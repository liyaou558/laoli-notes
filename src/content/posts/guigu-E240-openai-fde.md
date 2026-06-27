---
title: "一文 × Jove × Oliver｜OpenAI联手PE砸下40亿美元，聊硅谷最火新职位FDE"
description: '硅谷101深度解读FDE（前线部署工程师）：从Palantir起源、OpenAI收购Tomorrow获150名FDE、私募绕过咨询公司直接与模型公司合作的逻辑，到AI落地中最容易犯的错误，一站式理解Agent时代最火工种。'
date: 2026-06-18
category: "播客笔记"
tags: ["播客", "FDE", "OpenAI", "Anthropic", "AI落地", "私募股权", "Agent"]
podcast: "硅谷101"
guests: "Jove（Cresta FDE负责人）、Oliver（Invisible Technologies企业业务VP，前麦肯锡咨询师）"
duration: "51分钟"
---

> 播客：硅谷101 E240
> 主播：一文
> 嘉宾：Jove（Cresta FDE负责人）、Oliver（Invisible Technologies企业业务VP，前麦肯锡）
> 时长：约51分钟
> 来源：小宇宙
> 备注：基于 Whisper 转写整理

## 一、核心观点

### 1. FDE——硅谷最火新职位的本质：前线的 mini CTO

2026年5月，OpenAI宣布成立 Deployment Company（部署公司），同时收购 Tomorrow 公司带走150名FDE。同期 Anthropic 联手 Blackstone 等金融机构成立合资企业，Google 也组建了FDE团队。FDE（Forward Deployment Engineer，前线部署工程师）成为硅谷最热工种。Jove 用一句话定义：**FDE是跟客户紧密合作、让AI应用真正跑出来的工程师，同时承担把一线经验反馈回产品、让产品变更好的职责**——就像一个"前线的 mini CTO"。FDE跟客户共创AI方案，做完不是终点，后续的优化、监控同样耗费大量精力。

### 2. 模型公司集体觉醒：模型本身不是产品

OpenAI、Anthropic、Google 纷纷组建FDE团队，背后是同一个认知转变：**模型公司终于承认模型本身并不是产品，产品要落地还需要做大量工作**。企业买了模型也不知道怎么用，必须通过FDE这种贴身服务了解客户真正需要什么。模型公司与应用公司的边界因此变得模糊——模型公司不愿自己招大量人去做360行的落地，于是通过收购或资本合作来让别的公司做FDE。应用层公司则利用历史数据（如Cresta从2017年积累的客服对话数据）和模型选择自由度建立壁垒。

### 3. Palantir 是 FDE 模式的鼻祖

FDE这个工种已存在十几年，由 Palantir 首创。Palantir 的军方客户不愿把需求说清楚，必须跑到同一个军营帐篷、看到数据才愿意细说。Palantir 为此组建了两个团队：**Delta（偏技术，Forward Deployed Software Engineer）和 Echo（偏领域知识，熟悉作战/救援等业务）**，合在一起成为FDE。Cresta 借鉴了这个模式，演化为 FDE（像CTO，偏技术）+ FDPM（Forward Deployed Product Manager，像CEO，偏客户关系与需求把控），一个项目通常1个FDPM配2-3个FDE。

### 4. 私募基金绕过咨询公司直接找模型公司——三重动机

Oliver 拆解了PE与OpenAI/Anthropic合作的三重动机：

- **信号价值**：GP向LP募资时必须证明自己站在AI最前沿，否则LP不给钱。跟行业最响亮的名字（OpenAI/Anthropic）合作是最好的背书。
- **投资组合价值创造**：用AI改造投后公司是真实需求。SaaS已死论调让PE高度紧张——几乎所有PE都有软件公司敞口。
- **投资回报**：合作结构设计诱人，让GP进入高回报AI赛道。

相比找传统咨询公司"慢慢谈scope"，PE直接给CEO一个指标——"你就是要用FDE把业务AI化"——推进快得多。

### 5. AI时代的"收购-改造"模式：不只降本，更在增收

Oliver 指出，PE收购逻辑正在变为**AI Roll-up**——表面上买公司，实际买下工作流，再激进地用AI改造成AI Native公司。但他强调行业最大的误区是只把AI看作降本工具，**AI真正的价值在于创造收入**。他常问客户："如果免费给你一万个受过大学教育的员工，你过去想做但做不了的事是什么？"——因为这就是AI现在带来的能力。

### 6. 咨询行业不会消失，但会被重塑

Oliver 判断未来3-5年咨询将迎来增长——所有企业在探索AI时都需要重新思考商业模式。但**真正释放价值的是那些"做完走人、但留下一套改造好的业务"的模式**（如AI实验室和Invisible这样的公司），而不是只聊怎么转型。咨询的长期威胁在于：客户自己能用AI做的越来越多，传统外包的价值被侵蚀。

### 7. 独立AI应用公司的"模型自由"优势

Jove 指出，Cresta 一个对话中可能用到二十几个不同模型——挑最合适的而非最贵的，因为卖的是最终效果（Outcome）而非Token。这种选择自由度是大厂（Google必须推Gemini、OpenAI/Anthropic被自家模型绑定）不具备的。独立AI应用公司可以挑"刚好够用、价格合适"的模型，还能在断网时部署本地模型。

## 二、关键问答

**Q: FDE到底做什么？具体怎么改变企业工作流？**

以Cresta的AI客服Agent为例：FDE先从历史对话数据中分析哪些use case量大但SOP清晰（80%的volume来自20%的use case），然后用客户数据训练小模型做模拟测试。FDE跟客户共创——不是帮客户改一批数据就完事，而是一起做出AI进程，做大量测试优化。做完只是第一步，后续还有大量优化监控。

**Q: FDE在什么阶段介入客户？需要现场驻场吗？**

售前、售中、售后FDE都会参与。售前帮销售做功能级demo，售中做初期开发和调试，上线后监控指标达标即可退出——一个项目通常2-4个月FDE就退出。现场驻场一般不超过一周，通常是kick off时飞到客户办公室闭门开两三天会、做小型POC，之后远程协作，UAT（用户验收）时再聚。

**Q: 什么样的FDE是好的？怎么招？**

Jove 的招聘标准：①合格的工程师——AI Agent时代用Cursor/Claude Code写代码没问题，但必须知道怎么开发和测试AI Agent；②过硬的客户沟通能力——要跟对方CTO、IT Director级别的senior人员沟通，能简化复杂问题、敢于say no；③靠谱、有韧性、有agency——FDE面对的是"API纸糊的、SOP跟没有一样"的不完美世界。**不招任何Junior**，最喜欢招创始人/创始工程师。

**Q: FDE这个职位会被AI取代吗？**

短期（1-2年）：工具（如Gong录音翻译、Glean搜索）让FDE更高效，从同时做2-3个项目到5-6个。长期会分化：高端FDE做极难的事；长尾市场出现便宜的远程FDE（甚至越南等地）。**FDE要完全AI化路还很长**——FDE需要跟客户喝咖啡获取AI无法获得的context，需要为最终决定负责（skin in the game），AI可以出proposal但不能做决定。

**Q: PE投资组合中的传统企业（制造业、工业）怎么用AI改造？**

Oliver 强调AI创造价值最大的地方恰恰不是软件公司，而是**商业服务、工业、医疗**——那些原来软件不太能帮上忙的行业。他们帮一家乳制品公司整合数据并搭建AI系统为每头奶牛生成健康报告，让兽医把时间从写报告转到真正维护奶牛健康——这在过去不可行。

**Q: AI落地最常见的两个错误是什么？**

Oliver 指出：第一，**数据基础没打好**——AI再聪明没有数据什么都做不了。企业数据散落在Outlook、Gmail、LinkedIn、ERP、Salesforce等不同系统里，PE收购的公司可能跑着四套不同ERP。第二，**把本该确定性的步骤也交给AI**——十步的工作流，不是每一步都该用AI。账目对账等需要确定性结果的步骤应该硬编码做数学计算。

**Q: FDE的职业前景如何？**

Jove 认为FDE就像一个**创业训练营**——公司给你一个不舒服但成长极快的工作状态，锻炼技术、客户沟通、决策能力。一年不可能换三四份工作去不同公司体验，但做FDE有机会深入了解不同行业的运作。"人到最后的独特价值是成为AI的触手"——白天跟客户开会喝咖啡获取context，晚上对AI一顿输出把想法变成现实。

## 三、备忘

**关键数据与事实：**
- OpenAI收购Tomorrow获150名FDE，成立Deployment Company
- Anthropic联手Blackstone等PE成立合资企业
- Cresta从2017年开始积累客服对话数据（合规存储），是训练AI Agent的核心壁垒
- Cresta FDE团队规模：约百人团队
- 一个项目通常1个FDPM配2-3个FDE，FDE在项目2-4个月后退出
- FDE平均同时做2-3个项目，未来工具改进后可能到5-6个

**概念与术语：**
- **FDE (Forward Deployment Engineer)**：前线/前端部署工程师，负责将AI产品在企业客户中落地并将经验反馈回产品
- **FDPM (Forward Deployed Product Manager)**：前线部署产品经理，偏客户关系、需求把控和信任建立，像"前线的CEO"
- **Deployment Company**：OpenAI成立的部署公司，专门帮企业落地AI
- **AI Roll-up**：PE收购传统企业后用AI激进改造的投后策略
- **Palantir Delta & Echo**：Delta偏技术工程师，Echo偏领域知识专家——FDE模式的原型
- **Skills（Coding Agent的Skill）**：将FDE的经验写成可复用的Markdown+Script+Reference，新人装上就能用，形成"雪球效应"
- **Outcome-based pricing**：按结果收费而非按小时/token收费，AI时代咨询和律师事务所面临的定价模式转变

**Invisible Technologies 四大模块：**
- **Neuron**：数据层和数据网格，整合结构化和非结构化数据
- **Atomic**：梳理和自动化工作流
- **Synapse**：评估AI在工作流中的表现
- **Action**：协调工作流中的不同智能体
