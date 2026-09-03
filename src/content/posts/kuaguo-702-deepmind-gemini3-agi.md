---
title: '跨国串门儿 #702｜DeepMind CTO：AGI 不在实验室里，在真实用户与产品中被共同构建'
description: 'Google DeepMind CTO Koray Kavukcuoglu 谈 Gemini 3：benchmark 之外的进步、指令遵循、Vibe Coding 与通过产品构建 AGI'
date: 2026-09-04
category: "播客笔记"
tags: ["播客","AGI"]
podcast: "跨国串门儿计划"
guests: "Koray Kavukcuoglu"
duration: "52分钟"
---

> 播客：跨国串门儿计划 #702（约 52 分钟）。本集为 Google 官方英文播客 *Google AI: Release Notes* 的 AI 克隆中文版，主持人 Logan Kilpatrick，嘉宾是 Google DeepMind CTO、Google Chief AI Architect（首席 AI 架构师）Koray Kavukcuoglu。他 2012 年加入 DeepMind，是 DeepMind 第一位深度学习研究员之一，曾师从 NYU 的 Yann LeCun，参与了 Gemini、AlphaGo、AlphaFold 等核心项目。话题围绕 Gemini 3 的发布与「如何构建 AGI」。

## 一、核心观点

- **真正的检验是用户，不是 benchmark。** Gemini 3 发布之际，Koray 反复强调：模型真正的进步要到科学家、学生、律师、工程师手里去验证。benchmark 分数再高，都不等于现实世界中的能力，只有真实用户在真实任务里用起来，才构成「进步」的证据。

- **benchmark 会随着 frontier 前移而不断被「打穿」。** 从 Gemini 2.5 到 Gemini 3，HLE（Humanity's Last Exam）、ARC-AGI 2、GPQA Diamond 等榜单上的成绩在刷新，但也意味着旧的评估方式很快饱和，研究团队必须持续寻找并定义下一个 frontier，否则无法衡量真正的能力上限。

- **指令遵循是 Gemini 3 的重中之重。** 他特别强调模型要「学会不回答自以为该答的问题」——当指令与模型猜测冲突时，以指令为准；同时强化国际化、对非英语语言的支持，以及 Function calls、Tool calls、Agent 与代码相关能力，让模型真正成为可被调度的执行体。

- **Vibe Coding 正在把「有想法的人」变成「建设者」。** 让更多人通过自然语言/氛围式编程做出产品，是这一轮浪潮的意义所在；Google 的 Antigravity 是一个新的 Agent 式编程平台。同时 Koray 提到要让模型向真正的软件工程师学习，而不是只学公开代码。

- **通过产品构建 AGI。** Search AI Mode、AI Overview 等真实产品每天带来的用户反馈，是最宝贵的信号。他认为应该把 benchmark 与现实世界的产品信号结合起来，AGI 不是实验室里闭门造车的结果，而是在产品与真实用户的反复交互中被「共同构建」出来的。

- **Chief AI Architect 与 CTO 是同一件事的两面。** 面对新头衔，Koray 表示这两个职责本质上是统一的：既负责研究的方向与架构，也负责把研究落到可规模化的工程与产品里去，而不是研究归研究、工程归工程。

- **稳健性与安全必须内建，而不是事后打补丁。** 「Trusted-tested」的思路是把稳健性（robustness）与安全直接放进工程流程；安全从 pre-training 阶段就要开始考虑，贯穿训练到部署。Gemini 3 背后是 Google 全球范围内的跨团队协作。

- **享受成果的同时要诚实面对不足。** 即便 Gemini 3 已经很强，Koray 仍坦承：写作、编程（代码能力）、以及 Agent 的自主「行动」质量还有明显提升空间，多模态模型也远未到「到头了」的地步，前方仍有很多硬骨头。

## 二、关键问答

**Q：Gemini 3 发布了，衡量它成功最重要的标准是什么？**
A：不是某张 benchmark 榜单，而是它是否真正被用户用来解决现实问题。分数可以刷，但「用户在真实工作流里有没有因此变得更强」才说明问题。

**Q：为什么 benchmark 经常「不够用」了？**
A：因为前沿（frontier）本身在移动。HLE、ARC-AGI 2、GPQA Diamond 都是被设计来压住当时最前沿的任务，一旦模型追上来，它们就逐渐饱和，必须不断定义新任务、新评估来继续衡量真实能力。

**Q：Gemini 3 相比 2.5，在数据、预训练、后训练上做了什么？**
A：三者的创新都是持续的、彼此叠加的——更好的数据、更强的预训练与后训练管线，共同支撑了从 2.5 到 3 的跃升，不存在单一的「魔法」突破点。

**Q：你说的「指令遵循」具体指什么？**
A：关键是要避免模型「自作主张」。当用户指令与模型自己猜测的意图相冲突时，模型应当严格服从指令，而不是给出它自以为「更对」的答案。这是可用性最容易被忽略但影响最大的地方。

**Q：国际化 / 非英语支持为什么被单独拎出来讲？**
A：Gemini 的目标是全球用户，模型在英语之外语言上的表现同样关键，多语言能力是产品落地到不同市场的基础，也是这次重点打磨的能力之一。

**Q：Vibe Coding 会带来什么改变？**
A：它大幅降低了「从想法到产品」的门槛，让原本不写代码的人也能当建设者。Google 的 Antigravity 就是面向这种 Agent 式编程的新平台，而训练时让模型学习工程师真实的开发过程，效果会比只学公开代码更好。

**Q：产品反馈在 AGI 建设中扮演什么角色？**
A：Search AI Mode、AI Overview 这些真实产品每天产生海量真实交互数据，是最贴近现实世界的信号。把 benchmark 与现实产品反馈结合起来，才能知道模型在真实约束下到底行不行。

**Q：你现在的头衔是「Chief AI Architect」，这和 CTO 有什么区别？**
A：对我而言这是同一件事：既要定研究方向与系统架构，也要保证它能规模化落地到工程与产品。把研究与工程割裂开是错误的理解，两个头衔是对同一职责的不同侧写。

**Q：AGI 到底该怎么构建？**
A：不是实验室里单打独斗完成的项目。稳健性、安全、真实场景的适配都要融入流程，「我们就是要这样构建 AGI」——通过产品、用户与团队协作来共同逼近它。

**Q：你们怎么处理安全与稳健性？**
A：Trusted-tested 的思路是把稳健性和安全内置进工程流程，并且安全要从 pre-training 阶段就开始规划，而不是训练完再补救。Gemini 3 是 Google 全球协作的产物，靠的是跨团队合力。

**Q：Gemini 3 还有哪些不足，你愿意承认的？**
A：写作、编程以及 Agent 的实际「行动」仍不理想，多模态也还有很大空间。诚实面对这些不足，正是下一轮改进的起点。

## 三、备忘

- **嘉宾**：Koray Kavukcuoglu —— Google DeepMind CTO、Google Chief AI Architect；2012 年加入 DeepMind，是 DeepMind 第一位深度学习研究员；曾师从 NYU 的 Yann LeCun；参与 Gemini、AlphaGo、AlphaFold。
- **主持人**：Logan Kilpatrick。
- **节目**：《跨国串门儿计划》#702，源自英文播客 *Google AI: Release Notes*，AI 克隆为中文，约 52 分钟。
- **模型**：Gemini 3（对比对象 Gemini 2.5）。
- **Benchmark**：HLE（Humanity's Last Exam）、ARC-AGI 2、GPQA Diamond。
- **产品**：Search AI Mode、AI Overview、Google Antigravity（新的 Agent 式编程平台）。
- **关键能力点**：指令遵循、国际化/非英语支持、Function calls、Tool calls、Agent、代码。
- **方法论关键词**：Trusted-tested（稳健性与安全内建于工程流程）、安全从 pre-training 开始、benchmark × 真实产品信号、通过产品共同构建 AGI。

---

本文基于小宇宙 show notes 整理，非完整转录稿。
