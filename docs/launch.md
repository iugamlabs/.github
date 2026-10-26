# 品牌启动清单 / Brand launch checklist

## 已准备，随 PR 合并生效 / Prepared, effective after PR merges

- [x] 小写 iugam 定位、双语组织主页、公开项目目录与矢量素材 / Lowercase brand, bilingual profiles, public catalog and vector assets.
- [x] 新安装入口与老用户迁移说明 / New install commands and existing-user migration instructions.
- [x] 兼容性例外与旧品牌检查 / Compatibility exceptions and legacy-brand checks.

## 账号与域名 / Accounts and domain

- [ ] 在注册商确认 `iugam.com` 可购买性、归属和报价；本次不购买 / Confirm availability, ownership and price with a registrar; no purchase in this migration.
- [ ] 登录 npm 核实 `iugam` 用户与组织命名空间，若可用则创建 `@iugam`；本次不改现有包名 / Verify the npm namespace when signed in, claim it if available, and preserve existing package names.
- [ ] 将 `brand/avatar.svg` 导出的头像上传 GitHub 组织；CLI REST 不提供头像上传接口 / Upload an avatar exported from `brand/avatar.svg`; GitHub's organization REST API has no avatar-upload endpoint.
- [x] 通过已登录管理界面补查 Packages 与组织级 Actions，未发现待迁移的配置 / Reviewed Packages and organization Actions in the authenticated settings UI; no remaining brand configuration changes found.
- [ ] 核实 PyPI Trusted Publisher 的实际 owner、仓库、工作流和 environment 绑定 / Verify actual PyPI Trusted Publisher owner, repository, workflow and environment bindings.

## 官网首版 / Website v1

- [ ] 域名确定后建立 `/zh/` 与 `/en/`：首页、工具目录、项目介绍、品牌故事、联系入口 / After the domain is resolved, create `/zh/` and `/en/`: home, catalog, project details, story and contact.
- [ ] 从 `profile/projects.json` 读取公开项目；产品文档与问题反馈链接到各仓库 / Consume the shared public catalog and link documentation and feedback to each repository.
- [ ] 主要展示开发者与效率工具，Fork 注明来源，实验项目单列 / Feature developer and productivity tools, attribute forks and separate experiments.
- [ ] AI 产品使用各自产品名，品牌官网不复用旧 AI 工具箱的产品定位 / Keep AI product identities distinct from the main brand site.
- [ ] 配置品牌邮箱、GitHub 官网链接及相关公开渠道 / Configure brand email, GitHub website links and related public channels.

## 持续维护 / Maintenance

- [ ] 各仓库 PR 合并后重新扫描默认分支并验证安装、构建和发布通知 / Rescan default branches and verify installation, builds and release notifications after merges.
- [ ] 新增项目同时维护中英描述和上游来源 / Add Chinese and English descriptions and upstream attribution for new projects.
- [ ] 定期检查新旧安装入口、官网链接与公开目录 / Periodically check installation endpoints, website links and the public catalog.
