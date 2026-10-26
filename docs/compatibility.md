# 兼容性保留清单 / Compatibility exceptions

| 标识或记录 / Identifier or record | 原因 / Reason |
| --- | --- |
| `github.com/star-plan/wechatctl` | 现有 Go module、import 与 `go install` 路径；本轮不做破坏性改名 / Existing Go module, imports and installation path; no breaking rename in this migration. |
| `github.com/heyoungai/ship` | 现有 Go module、import、版本注入与安装路径 / Existing Go module, imports, version injection and installation path. |
| `docs/changes/20*.md`、`docs/changes/completed/*`、`docs/releases/v*.md` | 保留历史发布和决策记录 / Preserve historical release and decision records. |
| `docs/fork-merge-guide.md` | 保留组织改名及上游合并过程的解释 / Preserve explanations of the rename and upstream merge process. |
| `docs/migration.md` | 包含旧安装源的迁移示例 / Contains migration examples for existing installation sources. |

`scripts/check-brand.py` 仅豁免精确模块前缀和上述文档路径。活动方案、普通 README、清单与生成脚本继续接受检查。

`scripts/check-brand.py` permits only the exact module prefixes and documentation paths above. Active plans, ordinary READMEs, manifests and generators remain checked.
