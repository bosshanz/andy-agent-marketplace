# My Coding Skills

- 作者：[bosshanz](https://github.com/bosshanz)
- 来源：https://github.com/bosshanz/my-coding-skills
- 固定提交：`c143e517df6caf820caac10edbffe7cdf35d8c56`
- 许可证：MIT；内含设计参考的独立许可一并保留。
- 收录方式：原样复制 9 个 Skill 及资源到插件的 `skills/`，仅新增插件元数据。

## 推荐理由

把个人编码工作流整理成一套可复用能力：设计、按需业务验证、工程参考，以及明确指定后的外部 Agent 调用。普通实现由当前 Agent 直接完成。

## 什么时候用

需要具体设计决策、业务规则检查或验收、后端/存储/架构资料，或调用指定外部 CLI。例如：“$eng 看一下这个支付回调的幂等写入约束。”

`design` 负责 UI 和交互设计；独立架构图或流程图可使用 Diagram Design。`verify`、`eng` 和外部 Agent 仍要求原 Skill 定义的明确触发，不因打包而改变。

## 使用与验证

插件不会替你安装外部 CLI。已有独立安装的同名 Skill 时，选择一种安装方式，避免重复加载。当前验证范围是来源一致性、文件完整性与插件结构；未在新任务中验证插件命名空间下的跨 Skill 路由，也未运行外部 Agent。
