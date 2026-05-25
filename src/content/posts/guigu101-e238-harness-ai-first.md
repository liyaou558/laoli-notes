---
title: "E238｜聊聊Harness时代AI-First的组织架构：从信任人到信任AI"
description: '硅谷101与Creo三位创始人深聊Harness Engineering工程范式'
date: 2026-05-26
category: "播客笔记"
tags: ["播客", "AI", "组织架构"]
podcast: "硅谷101"
guests: "Kai、Peter、Clark"
duration: "65分钟"
---

> **播客**：硅谷101 E238
> **主持**：红军
> **嘉宾**：Kai（Creo CEO & Co-founder）、Peter（Creo CTO & Co-founder）、Clark（Creo Co-founder，Go-to-market）
> **来源**：https://guigu.fm
> **收听日期**：2026-05-26

## 一、核心观点

1. **Harness Engineering 是 2026 年 AI 工程化的新范式**：继 2023 Prompt Engineering 和 2024 Context Engineering 之后，Harness Engineering 成为硅谷热门概念——它不再只关注怎么跟大模型交互，而是如何围绕大模型搭建一套能在真实世界中持续工作、自我修复、自我提升的系统。Harness 涵盖了 Sandbox 架构、安全保证、工具链集成、CICD 自动化、延迟优化等全链路工程能力。

2. **真正的 AI-first 不是叠加 AI 工具，而是围绕 AI 重构工作流程与组织架构**：Creo 三位创始人反复强调，如果只是让每个人用 AI 写代码、写 PRD、做图，效率未必提升，反而因节奏不同导致对齐成本飙升。真正的转型是把生产力的主导者从人变成 AI，人退居"结果审查者"角色。

3. **从"信任人"到"信任 AI"是组织转型的核心挑战**：AI-first 组织需要建立一套"护栏"（guardrails）和机制去保障 AI 的所有决策、规划和执行都能被信任。信任不是天赋的，而是通过 Harness 系统逐步构建的——包括 AI-driven testing、自动 bug triage、数据信号反馈回路等。

4. **产品经理角色被"组织化"而非"个人化"**：Creo 内部拆解了传统 PM 岗位，产品 sense 融入工程师和架构师角色中。未来不再是某一个灵魂人物决定产品走向，而是整个组织通过 AI 的信号驱动形成产品判断。PM 不会消失，但会演变成具备 implementation 能力的复合型角色。

5. **初级工程师比资深工程师更容易适应 AI-first 环境**：Peter 在推文中指出，初级工程师的"技术惯性"更小、思想更灵活，能更快接受 expanded scope（不仅是写代码，还要参与产品设计、数据分析、判断 feature impact）。资深工程师在专业领域积累深厚，但转变 mindset 的难度更大，而那些能拥抱 AI 的资深工程师价值极高。

6. **开发速度远超市场营销速度，供需关系正被倒置**：AI-first 开发模式下，25 人团队 10 个工程师两周就能交付过去需 100 人四五个月的产品。结果是 feature 多到市场团队"追赶"不过来，团队从讨论 roadmap 变成根据市场需求从"菜篮子"里挑选已建好的功能。

7. **Agent 不需要价值观判断，Harness 解决的是效率问题**：当前 agent 的主要问题仍是 cost、latency、hallucination、tooling authentication 等工程效率层面的挑战。Harness 的核心目标是在最低成本下，reliable 地完成用户任务，通过 autofixing 系统已有 50% 以上的 issue 可以 AI 自动修复合入。

8. **SaaS 产品正在从"人看 Dashboard"转向"Agent 调 API/MCP"**：Creo 团队分享了对 SaaS 产品的观察——以前团队关心 Dashboard 好不好看，现在关心产品有没有好的 MCP 和 API 让 agent 直接调用。这个转变说明消费界面正在从"给人看"变成"给 agent 用"。

## 二、关键问答

**Q1: 什么是 Harness Engineering？与 Prompt Engineering 和 Context Engineering 的区别是什么？**
A: Harness Engineering 不再只聚焦于如何优化 prompt 或 context 跟单一模型交互，而是系统性地解决大模型在生产环境中持续运作的问题——包括工具调用、安全、Sandbox 架构、延迟、CICD、自我修复等全链路。Prompt/Context Engineering 是静态优化单一模型输出，Harness 是动态地让整个系统自我提升。

**Q2: 为什么多数公司所谓的"AI-first"是假的？**
A: 真正 AI-first 的核心是把 AI 作为生产力主导者，而不是人的辅助工具。大多数公司仍停留在"AI 帮人提效"阶段，人仍是驱动者，因此效率提升有天花板（最多 10 倍）。当 AI 成为主导，效率才能达到 100-1000 倍提升。

**Q3: AI-first 组织架构具体改变了什么？**
A: 第一，信任对象从人变成 AI 系统，需要建立 guardrails 机制保障 AI 决策可靠。第二，产品经理角色被拆解分散到工程师和架构师身上，对齐成本反而降低。第三，所有团队对齐不再靠开会沟通，而是由 AI 根据数据信号自动完成（如自动通知市场团队今天发布了什么功能）。

**Q4: AI 主导的开发流程如何运转？**
A: 工程师早上写 feature，中午 A/B test，下午根据数据反馈砍掉功能，5 点重写更好版本——传统开发需要 6 周的 cycle 现在一天内完成。代码 99% 由 AI 写，架构师（architecture）负责 criticise AI 的 plan 并优化系统级别问题（安全、延迟），不再手写代码。

**Q5: AI 写的代码质量如何保证？**
A: 通过 agent-driven CICD 和 agent-driven bug triage 系统。多路 agent 并行检测前端/后端/核心系统问题，发现 bug 只需 1-2 分钟，assign 给工程师只需几秒，整体 fix cycle 从一周缩短到 1-2 小时。50% 以上的 issue 通过 autofixing 自动完成，工程师只需 approve。

**Q6: 为何初级工程师比资深工程师更适合 AI-first 环境？**
A: 初级工程师技术惯性小、scope 更灵活，愿意接受从 coding 延伸到产品设计、数据分析的 expanded role。资深工程师往往高度专业化（做 infra 的不管部署后的表现），转变 mindset 需要更多时间。但能 embrace AI 的资深工程师价值极高——"之前需要 10-50 个，现在只需要 1-2 个"。

**Q7: AI 做 planning 的能力现在达到什么水平？**
A: Peter 评估，一年前 AI planning 能力约 50 分（不及格），现在能达到 90 分。他 2026 年全年没写一行代码，只通过 criticize AI 的 plan 来引导开发（例如指出安全缺陷、延迟隐患）。关键技巧是把经验沉淀为 skill，下次 AI 只需 reference 该 skill 即可遵循。

**Q8: Go-to-market 方面 agent 的应用挑战是什么？**
A: Clark 指出，engineering 领域 evaluation 相对容易（有明确指标），但 marketing 面对的是人的主观价值判断，如何把主观判断转化为系统信号是最大挑战。目前的做法是让 agent 生成大量素材，再由人判断效果后决定是否推向市场。

**Q9: 当前市场对 agent 的接受度如何？**
A: 核心挑战不是市场不能接受 agent 工作方式，而是市场根本不知道这种工作方式的存在。Creo 在做的事情是让用户无需复杂设置就能创建自己的 agent，提供 cloud 端 service 来隐藏架构复杂性，让非技术人员也能使用。

**Q10: 组织转型中最难的是什么？**
A: 是 mindset 的对齐。很多人愿意用 AI 工具提效（"用 AI 辅助"），但不愿意接受"AI 来 drive 工作、我的角色可能改变"。这两种心态是完全不同的。Creo 花了数月时间进行团队 mindset alignment，最核心的是让大家相信 AI 可以主导工作流。

**Q11: 如何看待 agent 经济——未来内容消费者是 agent 还是人？**
A: Clark 亲身经历：找合规公司时，第一步就是让 agent 做 research 和筛选。这意味着你的内容第一眼可能被 agent 消费。如果内容主要是给 agent 读的，那么"错误"的定义也随之改变——对人来说是致命错误，对 agent 可能不是。要根据内容消费者调整 Harness 系统。

**Q12: Creo 对比传统 agent 公司的差异是什么？**
A: 传统 general agent 公司提供一个 unique agent，所有用户 access 同一个。Creo 则让用户搭建属于自己的 agent，这些 agent 具有 self-improvement 和 self-healing 能力，能理解用户的工作流并持续优化。目标用户是 30 人以下的中小企业（SMB）。

**Q13: 为什么 AI-first 转型要从创始人开始？**
A: 大企业转型难的原因是合规问题和人的惯性阻力。中小企业如果没有老系统 legacy 负担，最容易转型。但创始人必须有核心信念——不仅是"用 AI"，而是理解转型意味着可能需要整体重构产品架构，接受不了这一点就很难成功。

## 三、备忘

- Peter 推文"为什么你的 AI 优先战略可能错了"在 Twitter 获得 187 万流量，是本期节目的核心话题起点
- Creo 2025 年 8-9 月开始意识到需要转型，2026 年 1 月用两周完成全面架构重构
- 关键词：self-healing、self-improvement、agent-driven CICD、autofixing、architecture vs operator、MCP/API 优先
- 金句：把 AI 当成系统看待而不是当成智能看待——当系统出错时不是去纠正智能，而是去弥补系统
- 警示：不要让 AI 仅仅成为效率工具，而是要让 AI 成为生产关系的中心
