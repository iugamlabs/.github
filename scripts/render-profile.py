"""从公开项目目录生成双语主页；--check 用于 CI 检查，不重写文件。"""
from pathlib import Path
import argparse
import json

ROOT = Path(__file__).resolve().parents[1]

def project_description(project, lang):
    """Fork 的上游地址也来自目录，避免在模板里写死某一个项目的来源。"""
    description = project['description'][lang]
    if project['fork']:
        label = '上游' if lang == 'zh' else 'Upstream'
        description += f" [{label}]({project['upstream_url']})"
    return description

def render(lang, projects):
    """两种语言共享同一项目集合，避免网站与 GitHub 主页分别维护。"""
    zh = lang == 'zh'
    lines = [
        '# iugam', '',
        '[中文](https://github.com/iugamlabs/.github/blob/master/profile/README.md) · [English](https://github.com/iugamlabs/.github/blob/master/profile/README.en.md)', '',
        '![iugam](https://raw.githubusercontent.com/iugamlabs/.github/master/brand/wordmark.svg)', '',
        '实用、轻量的开发者与效率工具。' if zh else 'Practical, lightweight tools for developers and everyday work.', '',
        'iugam 是一个独立开发品牌，名称来自潮州话中的油柑。我们构建解决具体问题的工具，也保留对新想法的探索。GitHub 账号为 **iugamlabs**。' if zh else 'iugam is an independent developer brand, named after the Teochew pronunciation of 油柑 (Indian gooseberry). We build tools for concrete problems and make room for new ideas. Our GitHub account is **iugamlabs**.', '',
        '## 精选工具' if zh else '## Featured tools', '',
        '| 项目 | 用途 |' if zh else '| Project | Purpose |', '| --- | --- |',
    ]
    # 精选标记和展示顺序都来自目录，官网无需再维护另一份名单。
    for p in projects:
        if not p['featured']:
            continue
        name = p['name']
        desc = project_description(p, lang)
        lines.append(f"| [{name}]({p['url']}) | {desc} |")
    lines += ['', '## 安装' if zh else '## Installation', '',
              '```bash', 'brew tap iugamlabs/tap', 'brew install ship', '```', '',
              '```powershell', 'scoop bucket add iugam https://github.com/iugamlabs/scoop', 'scoop install ship', '```', '',
              '各工具支持的平台和其他安装方式请查阅项目 README。' if zh else 'See each project README for supported platforms and alternative installation methods.', '',
              '## 项目目录' if zh else '## Project catalog', '']
    for category, title_zh, title_en in [('tools','工具','Tools'),('forks','Fork 与实验','Forks and experiments'),('infrastructure','分发与社区','Distribution and community')]:
        lines += ['### '+(title_zh if zh else title_en), '']
        for p in projects:
            if p['category'] == category:
                lines.append(f"- [{p['name']}]({p['url']}) — {project_description(p, lang)}")
        lines.append('')
    lines += ['## 文档与反馈' if zh else '## Documentation and feedback', '',
              '使用说明、版本下载与问题反馈都位于各项目仓库。Fork 保留上游归属，不代表上游官方发行版。' if zh else 'Documentation, releases and issue reporting live in each project repository. Forks retain upstream attribution and are not official upstream distributions.', '',
              '[迁移公告](https://github.com/iugamlabs/.github/blob/master/docs/migration.md) · [品牌规范](https://github.com/iugamlabs/.github/blob/master/brand/README.md)' if zh else '[Migration announcement](https://github.com/iugamlabs/.github/blob/master/docs/migration.md) · [Brand guide](https://github.com/iugamlabs/.github/blob/master/brand/README.md)', '']
    return '\n'.join(lines)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    catalog = json.loads((ROOT/'profile/projects.json').read_text())
    for lang, filename in [('zh','README.md'), ('en','README.en.md')]:
        target = ROOT/'profile'/filename
        content = render(lang, catalog['projects'])
        if args.check:
            if not target.exists() or target.read_text() != content:
                raise SystemExit(f'{filename} 与项目目录不一致，请运行 scripts/render-profile.py')
        else:
            target.write_text(content)

if __name__ == '__main__':
    main()
