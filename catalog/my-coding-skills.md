# My Coding Skills

- 作者：[bosshanz](https://github.com/bosshanz)
- 来源：https://github.com/bosshanz/my-coding-skills
- 固定提交：`794735122bc3bccf02a4036a050b1b08bfd89cb1`
- 许可证：MIT；内含设计参考的独立许可一并保留。
- 收录方式：原样复制 11 个 Skill 及资源到插件的 `skills/`，仅新增插件元数据。

## 推荐理由

把个人编码工作流整理成一套可复用能力：设计、交付、澄清、按需 QA、验收，以及明确指定后的外部 Agent 调用。

## 什么时候用

实现需求、修复问题、设计产品交互或对已完成实现做验收。例如：“使用 dev 修复切换简历时未保存内容丢失的问题。”

`design` 负责 UI 和交互设计；独立架构图或流程图可使用 Diagram Design。QA 和外部 Agent 仍要求原 Skill 定义的明确触发，不因打包而改变。

## 使用与验证

插件不会替你安装外部 CLI。已有独立安装的同名 Skill 时，选择一种安装方式，避免重复加载。当前验证范围是来源一致性、文件完整性与插件结构；未在新任务中验证插件命名空间下的跨 Skill 路由，也未运行外部 Agent。
