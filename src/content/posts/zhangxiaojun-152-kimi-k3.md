---
title: '领读Kimi K3技术报告：注意力设计之美、多教师蒸馏与开源MoE'
description: '张小珺邀请清华博士候选人孙宇涛逐章领读 Kimi K3 技术报告：从线性注意力三十年脉络讲到 Kimi Delta Attention、Gated MLA、Latent MoE、Muon 优化器与 Quantile Balancing，再到 WSD 学习率之争、多教师蒸馏与分布式训练 Infra，串联十余篇论文讲清每个设计"为什么这样做"。'
date: 2026-08-27
category: "播客笔记"
tags: ["播客", "AI", "Kimi", "大模型"]
podcast: "张小珺｜商业访谈录"
duration: "124分钟"
guests: "孙宇涛（清华大学计算机系博士候选人、上海创制学院普瑞学者）"
---

> 播客：张小珺｜商业访谈录

本期是学习播客：张小珺邀请清华大学计算机系博士候选人、上海创制学院普瑞学者孙宇涛，领读月之暗面 Kimi K3 技术报告。K3 是总参数 2.8T、激活参数约 100B、原生支持 1M 上下文、全量开源的 MoE 模型。孙宇涛从博士起研究 LLM 架构与预训练（代表作含 chunk-recurrent 线性注意力计算范式、YOKO、YOKO Universal 等），他以"打开历史脉络"的方式讲解 K3，串联了十余篇论文与技术博客，语速极快。

## 一、核心观点

1. **K3 的核心是"有效 scaling"而非架构噱头。** K3 总参数 2.8T、激活参数约 100B（K2 为 1T 总参 / 32.6B 激活，激活量扩大三倍多），上下文原生支持 1M tokens，是国内开源模型当时最大的量级。孙宇涛强调：随便起一个 2.8T 模型只训 100B token 是"无效 scaling"，而参数量仍是决定模型智能上限的第一性因素，K3 的价值在于把 2.8T 这个规模真正"跑出来"。

2. **注意力设计是 K3 架构创新的主线。** 线性注意力经历了"KV 外积求和 → RetNet 引入位置相关衰减与 chunk-recurrent 计算 → Mamba 位置相关衰减 → DeltaNet 提高容量 → Gated DeltaNet 融合衰减"的演进，K3 采用的 Kimi Delta Attention（KDA）把 Gated DeltaNet 的标量衰减升级为 channel-wise 衰减，表达能力严格更强，代价是 kernel 更难写，于是用 lower-bound decay 把 16-token tile 内的衰减限制在 BF16 动态范围内。

3. **混合注意力不是工程妥协，而是"无损甚至更好"的选择。** 在保持一定全注意力比例（业界常用线性:全注意力 ≈ 3:1）的前提下，混合注意力模型可以获得与全注意力相当甚至更好的长上下文表现，同时大幅降低推理成本。这一实验结论是混合注意力被大规模采用的根因。

4. **K3 把"训练稳定性"当作架构设计的硬约束。** Gated MLA（把混元团队的 Gated Attention 引入 MLA）提升训练稳定性且与 MLA 正交；C2GLU 用类 tanh 的 soft-clip 把 MLP 中间激活严格 bound 住（源自 SwiGLU 时代 hard clip 的升级）；Muon 优化器易产生 activation outlier，K2 用 QK Clip 压制、K3 在架构层面直接约束。苏剑林的观点是：任何优化器都会出 outlier，从架构下手才是本质解法。

5. **Quantile Balancing 是 Loss-free Routing 的"原理化"升级。** 苏剑林博客提出的 QB 用回归方式直接推导出 bias 的解析更新式，免去 Loss-free 的启发式调参，且让第一层 MoE 也能做负载均衡（此前团队被迫把前几层改成 Dense 来规避 Loss-free 失效）。K3 工程上采用值域分桶 histogram 统计代替精确分位数，解决几十 M token 大 batch 下不可计算的问题。

6. **Latent MoE 是"免费的午餐"：降通信不降能力。** 把 dispatch 的 hidden state 缩小 2-4 倍，用更大 FFN 中间维度或更多专家弥补参数量，恰当配置可完全保持标准 MoE 的效果，却大幅降低随 hidden size 与专家数增长的通信开销——推理 latency 的收益尤其显著（通信在 critical path 上无法完全掩盖）。K3 因此不必采用 DeepSeek 式跨 batch 精细 overlap，用 shared expert 计算即可藏住通信。

7. **后训练最值得学的两个选择：Cosine Decay 与 SFT 阶段才引入低精度。** 当全行业都转向 MiniCPM 提出的 WSD 时，K3 反其道用 Cosine Decay，理由是它只有"总 token 数 + 最大学习率"两个变量、更好调参（WSD 多一个 decay 比例变量，且最优学习率其实与总 token 数绑定）。低精度方面，DeepSeek V3 原生 FP8、V4 原生 W4A8，而 K3 先高精度预训练、在 SFT 阶段引入 QAT——项目管理上更保险，技术上也不损失（低精度从 scratch 引入并不会带来能力提升）。

8. **多教师蒸馏（OPD）成为后训练合版的"工业标准"。** On-Policy Distillation 最初用于大模型蒸馏小模型，现在主流是"自己蒸馏自己"：把不同能力的 reward model / RL 范式统一成不同教师模型，再做多教师合版。非技术原因是 Post-train 团队管理大幅简化（模型同构、数据异构），技术原因是不同 reward 体系难以一朝会而模型合版容易。小米、GLM 等均采用此做法。

9. **长上下文最优解：混合注意力下全注意力层直接去掉 RoPE。** RoPE 本质带来的是 recency bias，只对短上下文建模有效，对长文无帮助甚至有害。孙宇涛审稿时给过 strong accept 的工作证明：混合模型里线性注意力已注入位置信息，full attention 用 NoPE 表现更好、扩展长文无需调任何参数。K3 在长上下文全注意力部分下掉 RoPE。

10. **对行业的两点判断：技术无里程碑、K3 的本质是 size 上台阶。** 孙宇涛认为科学研究不存在跨越式提升，所谓 milestone 只是渐进改进的节点；K3 最 impressive 的是把激活参数做到 100B（比上一代多三倍多），这是需要魄力的非技术决策。他还给出"暴论"：大模型可能没有太大的架构创新了，后面都是改进性进步；AGI 之所以难，是因为它从未被 well-defined。

## 二、关键问答

**Q: 请先介绍你的研究方向和背景。**
A: 孙宇涛是清华计算机系博士候选人、上海创制学院普瑞学者，博士方向是大模型架构与预训练，从 2023 年开始围绕"推理高效性"做架构研究。他观察到业界方向已从性能导向转向效率导向：参数量是模型性能的主因，架构改进带来的性能增益微小，但不同架构的推理成本差异巨大、直接决定部署价格。

**Q: 你最早的工作是什么？**
A: 他早期参与 RetNet 相关工作，主要贡献是提出 chunk-recurrent 的线性注意力计算范式：在"全递归"与"并行表示"之间取折中，既享受整体计算复杂度收益，又能把 GPU 的 local 计算密度打满。这一范式后来被 Mamba2、Gated DeltaNet、Kimi Delta Attention 等所有线性注意力改进工作继承。

**Q: 为什么从纯线性注意力转向混合注意力？**
A: 纯线性注意力受限于有限状态空间，长上下文能力难以匹敌全注意力，作为纯线性模型是"失败尝试"。实验发现，混合注意力（线性+全注意力组合）在保持一定全注意力比例时可以获得无损甚至更好的长上下文表现——它不是工程上的 trade-off，而是能力上的"白拿"，因此被大规模采用。

**Q: YOKO 解决了什么问题？**
A: 孙宇涛的第二篇工作 YOKO（You Only KV-cache Once）的思路是：既然全上下文 kv cache 省不掉，就从"层间"维度省——所有层共享一份 kv cache，同时保留多层全注意力计算结构，模型结果与混合注意力基本等价；prefill 阶段只需算线性保留拿到 kv cache，可完全跳过全注意力，而 decode 能力不受损。kv cache 存储上已到极致：一份就是最少。

**Q: YOKO Universal 又做了什么？**
A: 它把 loop language model（固定参数、多次迭代提升 FLOPs）只放在 YOKO 的线性注意力部分，因为线性注意力 kv cache 微乎其微、额外计算也小，却能获得接近全注意力的能力。效果是用约两倍计算强度换来约两倍性能提升，而存储与 kv cache 开销保持不变。

**Q: Kimi Delta Attention 相比 Gated DeltaNet 改了什么？**
A: 主要区别在衰减项：Gated DeltaNet 每个 head 共享一个标量衰减系数（写 kernel 方便），KDA 把标量衰减升级为 channel-wise 衰减——每个 channel 衰减系数可不同，从公式上严格更强（可退化回均匀衰减），代价是 kernel 实现难度大增。

**Q: Lower-bound decay（衰减下限）是做什么的？**
A: 为了让 channel-wise decay 能高效 kernel 化，K3 仿照 RoPE"用绝对位置表示相对位置"的思路，让 q 做衰减、k 做反衰减，通过乘法结合律等价回递归形式。但这样 q/k 会乘除极小量，数值上必须控制在 BF16 动态范围内——KDA 限制 16-token tile 内衰减不超过 BF16 精度范围，本质是一种为 kernel 服务的 code design。

**Q: Gated MLA 是什么？为什么要引入？**
A: MLA 自 DeepSeek V2 提出，被 V3、Kimi K2 采用，作用是压缩 KV cache。混元团队（Gated Attention）发现门控能显著提升训练稳定性、防止训练崩溃，CM 后续模型（CM Next、3.5/3.6）均采用。K3 把门控与 MLA 正交结合：不破坏 MLA 推理性质，同时获得训练稳定性收益。

**Q: MLA 会成为长期共识吗？**
A: 孙宇涛认为 MLA 本质是大号 MQA，没有带来新东西，其收益大部分可被更好的 GQA 参数设计拿走；且 MLA 推理时计算远超建模能力，存在浪费。DeepSeek 罗福莉的观点是 MLA 适合 Chat 范式但不适合 Agent 范式，且与 MTP 收益不正交甚至互相冲突（memory-bound 下 MTP 加速比大减）。DeepSeek V4 因此改用大号 MQA + Sparse。

**Q: Attention Residual 这条研究线是怎么来的？**
A: 脉络是 ResNet（何恺明时代就讨论 Pre-LN/Post-LN 与稳定性）→ DenseNet（黄高，聚合所有浅层状态）→ Hyper-Connection（用比 hidden state 更大的容量表示深度状态，思想简洁但论文抽象、没出圈）→ Attention Residual。这类连接方式对推理几乎免费，且与参数量提升正交，所以大家乐于采用。

**Q: 这些连接工作里你觉得创新性最强的是哪个？**
A: 他最喜欢 DenseNet 和 Hyper-Connection：DenseNet 在无 attention 时代就把连接问题想透了；Hyper-Connection 是在 Transformer 时代把更强的连接方式重新带回来，后面的 Attention Residual、DeepSeek 的 MHC 本质上都是它的变体——MHC 比 HC 火，主要是因为它是 DeepSeek 的工作。

**Q: Latent MoE 的原理是什么？**
A: MoE 的 dispatch 通信量随专家激活数与 hidden size 线性增长，Latent MoE 先把 hidden state 线性投影压缩 2-4 倍再分发，压缩掉的参数量用更大 FFN 中间维度或更多专家补回。论文证明恰当配置可完全保持标准 MoE 的效果，同时大幅降低通信——推理收益大于训练收益，因为推理 latency 里通信在 critical path 上无法完全掩盖。

**Q: 为什么两个矩阵连乘中间要加 normalization？**
A: 两个矩阵连乘在表达能力上可以合二为一，但优化性质完全不同，直接连乘经常训练不稳定。MLA 和 Latent MoE 本质上都是"先降维投影再打回来"的两段线性，中间必须加 RMSNorm 控制 hidden state，这是架构设计的一条铁律。

**Q: C2GLU 是怎么来的？**
A: 大模型训练中 MLP 中间激活极易爆炸/出 outlier，早期 GPT-OS 用 hard clip（clip 到 5-10）从数学上严格限界；把 hard clip 换成 soft clip 就自然得到类 tanh 的门控算子。C2GLU 把所有可能无界的中间激活都用 tanh 上下界放缩 bound 住，保证训练稳定性——这也回应了 Muon 优化器更容易出 activation outlier 的问题。

**Q: 苏剑林怎么看 Muon 与 outlier 的关系？**
A: 苏剑林会反对"Muon 更容易出 outlier"的说法：任何优化器都会出现 outlier，Adam 也不是完全稳定的（DeepSeek V3 训练也有不稳定现象），只是出现早晚问题；从模型架构上直接约束才是本质方案。K2 时代 Muon 已配 VDK 与 QK Clip，K3 延续这一思路。

**Q: Quantile Balancing 与 Loss-free Routing 有何不同？**
A: Loss-free 用启发式更新 bias 控制专家负载，无严格收敛标准、与主模型更新耦合差，底层几层被迫去掉 MoE。QB 从回归推导直接得到 bias 的一步解析式，不需要调参（少一个类学习率参数），负载均衡能力更优，第一层也能正常 MoE。工程上 K3 用 sigmoid 值域分桶做 histogram 统计，替代几十 M token 大 batch 下不可行的精确分位数。

**Q: K3 为什么不用 Sparse Attention？**
A: 两个原因：一是 Sparse 在 decode 阶段加速极小——求 index 昂贵且在 Blackwell 上 overhead 更大（GLM 的 Index Cache 靠跨 4-8 层共享才缓解），而混合注意力里全注意力层不相邻，index 共享收益存疑；二是 Sparse 基本无法 from-scratch 训练，都是 post-train 从全注意力转化，且 K3 用了 MLA 转化更难。孙宇涛团队在 YOKO 上把 index 也做成"once"跨层分摊。

**Q: 混合注意力最主要的 trade-off 是什么？**
A: 是线性与全注意力的比例：线性占比越大加速越高，但要保持近似无损同时拿到加速，3:1（全注意力占约 1/4）是实验上稳妥的方案，再往上加速比就上不去了。

**Q: K3 为什么放弃 WSD 改用 Cosine Decay？**
A: WSD（MiniCPM 提出）的优势是前面学习率恒定、可中途自由选择总训练量，且把好数据集中在学习最快的 cooldown 阶段。但 K3 指出：最优学习率其实与总 token 数绑定（跑 10T 用 6e-4、跑 20T 用 3e-4），任意切换并不划算；Cosine Decay 只有两个变量、更好找超参，所以 K3 选择更经典的方式，最终 schedule efficiency 比 K2 高 2.5 倍。

**Q: 长上下文为什么要把 RoPE 下掉？**
A: RoPE 带来的是 recency bias，对短上下文建模有效，对长文无帮助甚至有负面影响，且扩长文要调参数。孙宇涛审过一篇 strong accept 的工作证明：混合注意力里线性注意力已注入位置信息，全注意力层改用 NoPE 表现更好、扩展 1M 无需调任何架构参数。K3 采用此方案，外推效果也好。

**Q: 低精度训练应该在什么阶段引入？**
A: DeepSeek V3 原生 FP8、V4 原生 W4A8，K3 选择先高精度预训练、SFT 阶段再引入低精度 QAT。理由有二：项目管理上高精度大训练更保险、不可控因素少；技术上低精度 from-scratch 引入并不会带来能力提升，只要训练量足够，何时引入结果差不多——SFT 阶段引入是更稳妥且无损失的选择。

**Q: 什么是 OPD 多教师蒸馏？为什么成为主流？**
A: On-Policy Distillation 源自 MiniLM 的反向蒸馏：让学生生成答案、教师逐步纠正推理（ReverseKL），比直接学教师答案更有效。最初用于大模型蒸馏小模型，现在主流是"自己蒸馏自己"：把可验证 reward、reward model 等不同 RL 范式统一成多个教师模型再合版。非技术原因是 Post-train 团队管理简化，技术原因是模型同构、合版远比 reward 体系合版容易。

**Q: Draft Model / MTP 有哪些前沿做法？**
A: EAGLE-3 和 MTP 的思想是利用大模型中间层 hidden state 做投机解码，小模型可更小、接受率更高，且 MTP 需要在预训练阶段就预留接口。Diflash 把 Diffusion LLM 引入投机解码，单用户小 batch 场景快，但 from-scratch 训练效率低。小米 1000 TPS 方案 = 融合算子（约 300 TPS）+ Dflash + 投机推理叠加。孙宇涛预测 MTP 还有更深层工作。

**Q: KDA 的上下文并行（CP）特殊在哪？**
A: 全注意力 CP 概念简单（ring attention 等，把 kv cache 跨 GPU 聚合即可）；线性注意力的 CP 利用了 chunk 可任意拆分的数学性质：先按大 chunk（如 8K token/卡）跨机器做递归，内部再拆 16-tile chunk 并行计算，形成"双层 chunk"方案——这是 full attention 没有的自由度。

**Q: MNEP 动态专家并行解决了什么？**
A: 传统 EP 下 token 自由选专家导致各卡 token 数不均、执行时间互相等，通信还多一个"告知接收量"的阶段。MNEP 增加少量冗余专家，数学上证明只需小比例冗余即可让每卡 token 数完全对齐（online planning 提前规划），达到卡级均衡；但专家级均衡做不到，只能靠有损策略。

**Q: K3 的通信隐藏策略和 DeepSeek 有何不同？**
A: DeepSeek V3 需要把 MoE 的 dispatch/combine 拆到原子级、跨 batch 融合前后向重排，还引入 DuPipe 流水线。K3 因 Latent MoE 通信量极小，只需在单 batch 内部把 MoE 前后向通信与 shared expert 计算 overlap 即可，推理 critical path 的 latency 几乎免费；PP 上则把显存压力大的 rank 的 activation 转移给压力小的 rank，绕开复杂流水线设计。

**Q: 多模态给 Infra 带来哪些额外麻烦？**
A: 一是视觉编码器接入前有 token 压缩（如 32K→8K），编码器内部计算更长、可能要单独开 CP；二是原生 VL 训练时各卡文本/视觉比例不均会破坏 PP 流水线打满，K3 把视觉编码器放在 PP 中间或尾部，利用闲置段提前算视觉步骤来规避首段气泡。

**Q: RL 训练有什么值得说的工程细节？**
A: 一是每个 trajectory 对应一个 Docker，大规模 Sandbox/Docker 管理很麻烦；二是显存技巧：reference model 无梯度且 forward 完就不再使用，K3 把它的显存与 gradient buffer 合并复用（gradient buffer for non-policy model for forwarding），在 policy/reference/reward 多模型并存时显著省显存。

**Q: 线性注意力给推理引擎带来什么新问题？**
A: prefix cache 变难：full attention 每个位置的 cache 是上一个的简单增量，线性注意力每步复写 cache、prefix state 各不相同。当前策略是按 block 切、逐 block 做 prefix caching；VLM 混合架构里 full attention 可按配置管理 cache，线性注意力不能，推理引擎需要兼容性处理。

**Q: K3 最让你 impressed 的地方是什么？**
A: 是把激活参数做到 100B——比他预期还大，比上一代多三倍多，在已有开源模型 size 基础上提升了一个数量级。他认为这是非技术性的决策（不依赖任何特定技术能力，取决于你想达到什么效果），但需要魄力，呼应杨植麟说的"有概率的非共识"。

**Q: K3 和 DeepSeek V4 的区别是什么？**
A: 孙宇涛认为两者定位完全不同：DeepSeek 更强调性价比（1.2T 档 + Flash 小档，Flash 做得很好），Kimi 主要精力在提升开源模型能力上界、性价比不是首要考虑（K3 推理价格比别家贵很多）。技术之外，团队走向取决于人的选择，而技术好坏有客观标准、大家都不笨。

**Q: 有人说 Kimi 的研究方式比较科学，你认同吗？**
A: 认同。Kimi 公开强调"模型内科"：让不同行为 trace 以可靠方式获取、让模型不稳定或 collapse 能明确归因，这是科学化的体现。科学对应的是不科学——基于利益需求把科学方法干掉就是不科学。Kimi 团队非常团结、能把劲往一处使，判断方式自然而然就科学。

**Q: 对未来模型发展有什么预测？**
A: 他的"暴论"是：大模型可能没有太多大的创新了，后面都是改进性进步；模型 size 会继续扩大，但不可能无限——人类互联网可集结的数据量有限，模型没必要无限。纯语言 scope 内，只要能力能被清晰定义（coding、agent 任务）就能达成；AGI 难在从未被 well-defined，若定义包含真实物理世界交互，gap 还很大。

## 三、备忘

- **K3 关键数字**：总参数 2.8T、激活约 100B、上下文 1M tokens、全量开源；K2 为 1T 总参 / 32.6B 激活；K3 相对 K2 的 schedule efficiency 为 2.5 倍。
- **孙宇涛代表作**：RetNet 相关（chunk-recurrent 计算范式）、YOKO（全层共享 kv cache）、YOKO Universal（loop language model）、YOKO 上的 sparse index once。
- **线性注意力演进链**：KV 外积 → RetNet（位置相关衰减 + chunk recurrent）→ Mamba → DeltaNet → Gated DeltaNet → Kimi Delta Attention（channel-wise decay + lower-bound decay，16-token tile）。
- **连接方式演进链**：ResNet（Pre-LN/Post-LN）→ DenseNet → Hyper-Connection → Attention Residual → MHC（DeepSeek）。
- **混合比**：线性:全注意力 ≈ 3:1 为业界稳妥配置；全注意力占约 1/4，加速比上限约 4 倍。
- **优化器**：Muon（K2 沿用，配 VDK + QK Clip）；DeepSeek V4 / 其他团队用 Muon + GQA + QK Norm（更简单）；苏剑林：任何优化器都会出 outlier，架构约束才是本质。
- **Quantile Balancing**：苏剑林博客提出（非论文）；K3 工程实现 = sigmoid 值域分桶 histogram 统计，常数存储、易分布式扩展。
- **学习率**：WSD 由 MiniCPM 提出；K3 反用 Cosine Decay（两变量更好调）；低精度训练：DeepSeek V3 原生 FP8、V4 原生 W4A8、K3 在 SFT 阶段引入 QAT。
- **蒸馏**：OPD/On-Policy Distillation（源自 MiniLM ReverseKL，董老师团队、清华特奖得主郁贤做过相关 RM 工作）；多教师合版为业界标准（小米、GLM 均采用）。
- **投机解码**：EAGLE-3、MTP（需预训练留接口）、Diflash（Diffusion LLM）；小米 1000 TPS = 融合算子（约 300 TPS）+ Dflash + 投机推理。
- **Infra**：KDA 双层 chunk CP；MNEP 冗余专家动态 EP（卡级均衡）；Latent MoE 通信小 → shared expert overlap；PP 显存转移；视觉编码器放 PP 中尾部；RL 中 reference model 与 gradient buffer 复用；线性注意力按 block 做 prefix cache。
- **Sparse Attention**：decode 加速小（index 昂贵、Blackwell overhead 大）；GLM Index Cache 跨 4-8 层共享 index；K3 不用 sparse 的原因：混合架构 index 共享收益存疑 + 无法 from-scratch 训练。
- **NoPE**：混合注意力下全注意力层去掉 RoPE（Cohere 系工作，孙宇涛审稿给 strong accept）；RoPE 只带来 recency bias，对长文无益。
- **相关人物**：苏剑林（Kimi 科学家）、杨植麟（Kimi 创始人）、罗福莉（DeepSeek，谈 MLA 与 Agent）、何恺明（ResNet）、黄高（DenseNet）。
- **金句**："大模型可能没有太大的创新了"（孙宇涛暴论）；"谁有道理谁说了算"（Kimi 团队文化）；"AGI 最大的问题是没有被 well-defined"。

> 来源：小宇宙
