# iugam 品牌迁移 / Brand migration

## 中文

Star Plan 现统一为 **iugam**。GitHub 组织地址为 https://github.com/iugamlabs 。名称来自潮州话中的油柑，我们继续打造实用、轻量的开发者与效率工具。

### 新安装入口

```bash
brew tap iugamlabs/tap
brew install ship
```

```powershell
scoop bucket add iugam https://github.com/iugamlabs/scoop
scoop install ship
```

已有用户无需卸载应用。先更新旧源地址，确认更新成功，再选择是否使用新的源名称：

```bash
git -C "$(brew --repository star-plan/tap)" remote set-url origin https://github.com/iugamlabs/homebrew-tap
brew update
```

```powershell
git -C "$env:USERPROFILE\scoop\buckets\star-plan" remote set-url origin https://github.com/iugamlabs/scoop
scoop update
```

Scoop 使用自定义安装目录时，请将上述路径替换为 `$env:SCOOP\buckets\star-plan`。旧 bucket/tap 本地名称可继续保留，不要同时添加两个名称相同内容的源。若本地 bucket 名是 `iugamlabs`，同样只更新该目录的 remote。

包名、CLI 命令、配置与数据目录保持不变。`wechatctl` 的 `github.com/star-plan/wechatctl`、`ship` 的 `github.com/heyoungai/ship` 是暂时保留的 Go module 路径；对应 `go install` 和构建路径继续使用原值。`aiquokka` 已使用 `github.com/iugamlabs/aiquokka`。

历史 tag、Release 二进制和校验值保持不变。历史文档可能出现旧品牌；后续技术标识迁移将独立公告。

## English

Star Plan is now **iugam**, hosted at https://github.com/iugamlabs . The name comes from the Teochew pronunciation of 油柑 (Indian gooseberry). We continue to build practical, lightweight tools for developers and everyday work.

For new installations, use `brew tap iugamlabs/tap` or `scoop bucket add iugam https://github.com/iugamlabs/scoop`, followed by the existing install command.

Existing users can keep installed applications and the local bucket/tap name. Update its Git remote using the commands above, then run `brew update` or `scoop update`. Replace the Scoop path with `$env:SCOOP\buckets\star-plan` for custom installations, or use your existing `iugamlabs` bucket directory. Avoid adding duplicate sources.

Package names, commands, configuration and data directories remain unchanged. The Go module paths `github.com/star-plan/wechatctl` and `github.com/heyoungai/ship` remain supported compatibility identifiers; keep using them in `go install`, imports and build flags. `aiquokka` already uses `github.com/iugamlabs/aiquokka`.

Existing tags, release binaries and checksums are unchanged. Historical documents may retain the former name. Any future technical identifier migration will be announced separately.
