"""扫描 Git 跟踪文本；兼容模块、迁移示例与明确的历史记录可保留旧名。"""
from pathlib import Path
import argparse
import fnmatch
import re
import subprocess

LEGACY = re.compile(r"star[-_ ]?plan|heyoungai[/]ship", re.I)
# 只豁免旧模块的匹配区间；同一行额外出现的旧 owner 仍然会被检查。
MODULES = re.compile(r"(?<![\w./:])github[.]com/(?:star[-]plan/wechatctl|heyoungai[/]ship)(?=[/@`\s\"']|$)")
HISTORY = [
    'docs/changes/20*.md', 'docs/changes/completed/*',
    'docs/releases/v*.md', 'docs/fork-merge-guide.md',
]
MIGRATION = ['docs/migration.md']

def violations(path, text):
    """解释性迁移文档及历史记录按路径保留，普通文档仅豁免精确模块前缀。"""
    if any(fnmatch.fnmatch(path, pattern) for pattern in HISTORY + MIGRATION):
        return []
    result = []
    for number, line in enumerate(text.splitlines(), 1):
        compatible = [match.span() for match in MODULES.finditer(line)]
        for match in LEGACY.finditer(line):
            if not any(start <= match.start() and match.end() <= end for start, end in compatible):
                result.append((number, line.strip()))
                break
    return result

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()
    tracked = subprocess.check_output(['git', '-C', str(root), 'ls-files', '-z']).decode().split('\0')
    count = 0
    for relative in filter(None, tracked):
        path = root / relative
        # 不跟随符号链接，不读取依赖目录和大体积或二进制制品。
        if path.is_symlink() or not path.is_file() or path.stat().st_size > 2_000_000:
            continue
        if set(path.parts) & {'node_modules', 'vendor', '.venv', 'dist', 'build', 'obj', 'bin'}:
            continue
        data = path.read_bytes()
        if b'\0' in data:
            continue
        try:
            content = data.decode('utf-8')
        except UnicodeDecodeError:
            continue
        for number, line in violations(relative, content):
            print(f'{relative}:{number}: {line}')
            count += 1
    if count:
        raise SystemExit(f'{count} 处旧品牌引用需要迁移，或记录为明确的兼容例外。')
    print('Brand reference check passed.')

if __name__ == '__main__':
    main()
