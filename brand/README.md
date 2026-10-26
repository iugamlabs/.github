# iugam 品牌规范 / Brand guide

主品牌与字标统一为小写 **iugam**。GitHub 账号为 **iugamlabs**；它是平台标识，不替代品牌名称。

The brand and wordmark use lowercase **iugam**. **iugamlabs** is the GitHub account identifier.

名称来自潮州话中的油柑。品牌专注实用、轻量的开发者与效率工具，实验项目保留探索空间。

The name comes from the Teochew pronunciation of 油柑 (Indian gooseberry). iugam builds practical, lightweight tools for developers and everyday work, with room for experiments.

## 素材 / Assets

- `avatar.svg` / `avatar.png`：油柑图形头像 / Indian gooseberry avatar.
- `wordmark.svg` / `wordmark.png`：小写字标 / Lowercase wordmark.
- 主色 / Primary: `#173B31`; 果色 / Fruit: `#D6E69A`; 辅色 / Accent: `#83B89A`.
- 不重命名既有产品、命令、包和数据目录；Fork 应注明来源。
- Preserve existing product, command, package and data directory names. Attribute upstream forks.

## 内容源 / Content source

`profile/projects.json` 是公开项目目录的唯一来源，组织主页由 `scripts/render-profile.py` 生成。未来官网的 `/zh/` 与 `/en/` 也读取此目录，不复制维护项目列表。

`profile/projects.json` is the source for the public project catalog. Generate profiles with `scripts/render-profile.py`; the future `/zh/` and `/en/` website should consume the same catalog.

```bash
uv run --no-project python scripts/render-profile.py
uv run --no-project python scripts/render-profile.py --check
```
