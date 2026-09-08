# Andy’s Agent Marketplace

Andy 精选的 Skill / Plugin 安装目录。编码工作流继续在原仓库开发，这里维护收录理由、固定版本和 Codex 安装入口。

| 插件 | 用途 | 收录说明 |
| --- | --- | --- |
| My Coding Skills | 设计、开发、按需 QA、验收、外部 Agent 适配器 | [详情](catalog/my-coding-skills.md) |
| Diagram Design | 架构图、流程图等 HTML / SVG 图表 | [详情](catalog/diagram-design.md) |

## 在 Codex 中使用

从本仓库根目录注册市场：

```sh
codex plugin marketplace add .
codex plugin list
```

注册市场不会自动安装插件。通过 Codex 插件目录按需安装，或执行：

```sh
codex plugin add diagram-design@andy-agent-marketplace
# 已通过独立 Skill 方式安装 My Coding Skills 时，先处理重复安装，再选用插件版本。
codex plugin add my-coding-skills@andy-agent-marketplace
```

安装后新建任务，使新插件可被加载。这里注册的是自定义市场，不代表进入官方公共插件目录。

GitHub 发布后，可把第一条命令中的 `.` 换成实际的 `owner/repo`。此仓库第一版只提供 Codex 市场配置；其他 Agent 的安装方式见各上游 README，未在这里验证兼容性。

## 固定版本

- My Coding Skills：`0.4.0`，`794735122bc3bccf02a4036a050b1b08bfd89cb1`，原样打包 11 个 Skill 及其资源。
- Diagram Design：`2724fd2efd8c6737f6fa704fbf5da52d67375497`，直接引用上游插件，安装时需要网络。

完整版本和打包文件摘要见 [sources.lock.json](sources.lock.json)。结构验证不等于实际任务效果验证；当前还没有对两个插件执行模型行为测试。

## 维护

1. 新条目先写 `catalog/<name>.md`：推荐理由、场景、作者、许可证、来源版本、验证范围。
2. 已有插件优先用 Git 来源并固定完整 commit SHA；纯 Skill 才添加包装；要修改内容时 Fork。
3. 检查上游差异并试用后再更新固定版本；不自动跟随 `main`。
4. 同步维护市场索引与 `sources.lock.json`，运行 `python3 scripts/verify.py`。
5. My Coding Skills 的打包文件应来自指定提交，使用 `python3 scripts/sync_coding_skills.py /path/to/my-coding-skills FULL_COMMIT_SHA` 同步，然后复核差异。脚本不会注册或安装插件。

收录不代表默认启用。优先显式指定能力；多个插件覆盖同一任务时，按条目说明选择。

## 目录与许可

- `.agents/plugins/marketplace.json`：Codex 市场索引。
- `catalog/`：人工维护的精选说明。
- `plugins/my-coding-skills/`：固定版本的打包产物，保留原文与原许可。
- `sources.lock.json`：来源、提交和打包文件 SHA-256。

市场原创配置、文档与脚本采用 MIT；收录内容继续遵循各自许可证，详见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。
