---
description: "Use when creating, expanding, reviewing, or reorganizing a genre directory, topic folder, 题材目录, 写作研究 folder, or new subject-specific writing assets in this repository. Covers top-level genre naming, default folder template, what belongs in genre folders, and how to avoid mixing genre assets with 通用skills, scripts, or 仅用于参考."
name: "新增题材目录模板"
---

# 新增题材目录模板

适用于本项目中新建、扩展、整理题材目录时的默认做法。

## 题材目录的判断规则

若某一类内容明确服务于某个题材，而不是跨题材通用能力，则应放入对应题材目录。

这个判断不是只在新建目录时做一次，而应在后续向题材目录中补 Prompt、Skill、Agent、instructions、模板或检查清单时持续重复执行。

- 只要识别出新增内容里有一部分其实不专属于该题材，而是可跨题材复用的通用能力，就不应只留在题材目录内
- 对于这类内容，应无论本次任务是否显式要求修改通用 Skill，都同步考虑将其提取并沉淀到 `通用skills/` 中对应能力的通用 Skill
- 若对应通用 Skill 尚未存在，应优先补建通用 Skill，再让题材目录内资产回到题材入口、题材边界或题材包装层职责

不要把以下内容误放到题材目录：

- 通用 Skill
- 通用脚本
- 纯外部参考且与具体题材无关的资料

## 一级目录命名规则

- 一级题材目录名应使用中文
- 题材名应明确、可读、可直接用于 Skill 前缀
- 新建题材目录前，先确认不是现有题材目录的近义重复命名

## 题材目录的默认模板

新建题材目录时，默认至少包含：

```text
题材名/
  写作研究/
  .github/
    prompts/
    skills/
    agents/
    instructions/
```

说明：

- `写作研究/` 是默认研究资料落位
- `.github/` 是题材目录下的主工作目录，用于承载该题材的可执行 AI 资产
- `.github/prompts/` 用于放题材专属 Prompt
- `.github/skills/` 用于放题材专属 Skill
- `.github/agents/` 用于放题材专属 Agent
- `.github/instructions/` 用于放该题材范围内生效的局部 instructions
- 题材 Prompt frontmatter 中声明的 `agent` 默认指向同题材目录下 `.github/agents/` 中的 Agent；若工具链给出“未知智能体”之类告警，默认应忽略，不要仅因告警就随意改动既有 `agent:` 声明
- 题材相关的提示词、Skill、Agent、局部指令、写作参考、调查研究等内容，都应归属于该题材目录
- 不要为了“看起来完整”而预先创建大量空目录

## 可按需扩展的内容类型

当任务确有需要时，可在题材目录下继续承载：

- 题材专属 Skill
- 题材专属提示词
- 题材专属 Agent
- 题材专属局部 instructions
- 题材写作参考
- 题材调查研究
- 题材专属审阅或输出能力

扩展原则：按实际任务需要创建，不为了模板而堆空结构。

## 与其它目录的边界

- 与题材无关的可复用能力 → 放 `通用skills/`
- 与某个 Skill 无直接绑定的通用脚本 → 放 `scripts/`
- 来自外部、且与具体题材无关的参考资料 → 放 `仅用于参考/`
- 与某个题材强相关的内容 → 放对应题材目录

补充要求：

- 若你是在编写或修改题材目录内的 Skill、Prompt、局部 instructions 或其模板时，才识别出其中混入了题材无关的通用内容，也仍应把这部分内容回收到 `通用skills/`，而不是因为“当前正在处理题材目录”就继续留在题材层
- 题材目录中的资产应优先承载题材专属边界、题材入口兼容性、题材补充规则与题材研究沉淀，不应长期寄存本应上收到通用层的共性本体

## 题材目录中的 Skill 命名规则

如果在题材目录下新增 Skill：

- Skill 目录名必须以 `题材名-` 为前缀
- Skill 名称必须以 `题材名-` 为前缀
- 示例：`都市悬疑-设计人物传记`

## 新增题材目录时的默认检查项

- 该内容是否真的属于题材专属，而不是通用能力
- 一级目录名是否为中文
- 是否与现有题材目录重复或高度近义
- 是否至少包含 `写作研究/` 与 `.github/`
- `.github/` 下是否按需要包含 `prompts/`、`skills/`、`agents/`、`instructions/`
- 是否把本该去 `通用skills/`、`scripts/`、`仅用于参考/` 的内容误放进来了
- 若后续计划在该题材目录内补 Skill 或模板，是否已经预先考虑哪些部分其实应先沉淀为通用 Skill
- 若创建题材 Skill，Skill 名称和目录名前缀是否正确

## 推荐创建顺序

1. 先确定题材名
2. 创建题材一级目录
3. 创建 `写作研究/`
4. 创建 `.github/`
5. 在 `.github/` 下按需补充 `prompts/`、`skills/`、`agents/`、`instructions/`
6. 再根据真实需求补充题材 Skill、提示词、Agent、局部规则或参考资料
7. 最后检查命名、前缀与落位是否符合仓库规范

## 不推荐做法

- 先建一套很大的空目录骨架，后面长期不用
- 题材目录名使用英文或中英混搭
- 把通用能力塞进题材目录
- 明知新增内容已经是题材无关的共性规则，却因为本次只在改题材目录而不回收到 `通用skills/`
- 为同一题材反复新建近义目录
