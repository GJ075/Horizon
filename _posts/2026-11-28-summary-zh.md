---
layout: default
title: "Horizon Summary: 2026-11-28 (ZH)"
date: 2026-11-28
lang: zh
---

> 从 37 条内容中筛选出 17 条重要资讯。

---

**科技新闻**
1. [OpenSec 披露 Linux nfsd 预认证漏洞，可无登录获取 root](#item-tech-news-1) ⭐️ 9.0/10
2. [Unkernel：将真实 Linux 内核编译为 WebAssembly](#item-tech-news-2) ⭐️ 8.0/10
3. [WebRTC 被用于购物网站信用卡盗刷脚本](#item-tech-news-3) ⭐️ 7.0/10
4. [Google DeepCrossAttention：跨层注意力实现最高 3 倍加速](#item-tech-news-4) ⭐️ 7.0/10
5. [多州总检察长起诉 SpaceX，要求阻止 Grok 生成儿童性虐待与报复性色情图像](#item-tech-news-5) ⭐️ 7.0/10
6. [计算机验证的证明也可能为假](#item-tech-news-6) ⭐️ 7.0/10
7. [SemiAnalysis 深度解析 Trainium3 推理与微架构](#item-tech-news-7) ⭐️ 7.0/10
8. [黑客借 AI 工具 Artex 攻击美情报机构](#item-tech-news-8) ⭐️ 7.0/10
9. [Anthropic 系统卡披露暗中削弱模型研发请求](#item-tech-news-9) ⭐️ 7.0/10
10. [《我的世界》基岩版资源包漏洞影响 26.52 至 26.63，26.65 已修复](#item-tech-news-10) ⭐️ 7.0/10

**财经新闻**
1. [标普 500 进入回调区间，但熊市与衰退未必随之而来](#item-finance-news-1) ⭐️ 7.0/10
2. [央行发布大额存单新规：个人起购门槛降至 10 万元](#item-finance-news-2) ⭐️ 7.0/10
3. [市场监管总局约谈雅迪、台铃、爱玛等 15 家电动自行车企业](#item-finance-news-3) ⭐️ 7.0/10
4. [智利监管机构起诉苹果，寻求 8000 万美元罚款并要求开放应用分发](#item-finance-news-4) ⭐️ 7.0/10

**校招岗位**
1. [携程 2027 届秋招 AI Agent 云原生研发岗](#item-campus-jobs-1) ⭐️ 9.0/10
2. [华为 2027 届 AI 应用工程师本科可投](#item-campus-jobs-2) ⭐️ 7.0/10
3. [字节跳动杭州 AI Agent 开发工程师本科可投](#item-campus-jobs-3) ⭐️ 6.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [OpenSec 披露 Linux nfsd 预认证漏洞，可无登录获取 root](https://opensec.in/blog/nfs2root-cve-2026-99362) ⭐️ 9.0/10

OpenSec 披露了 Linux 内核 NFS 服务器 nfsd 的预认证堆溢出漏洞 CVE-2026-99362，CVSS 评分 9.8。攻击者无需登录，只需向 tcp/2049 发送一条连接即可越界写入内核堆，进而获得 root shell。该漏洞自 2014 年的 Linux 3.16 起存在，影响启用 NFSv4.1 或 4.2 的主机，波及文件服务器、NAS 和集群存储节点。修复已在 6.12.117、6.18.61、7.3.2 和 7.4-rc1 中发布，CVE 于 2026 年 11 月 20 日公开；上述信息来自 OpenSec 单一来源，尚无独立验证或技术细节披露。

telegram · zaihuapd · 11月27日 12:57

**「背景」** 该漏洞位于 Linux 内核的 NFS 服务器组件 nfsd，影响在可访问的 tcp/2049 端口上提供 NFSv4.1 或 4.2 服务的主机，而 4.1/4.2 是较新内核的默认配置。据 OpenSec 的披露，该缺陷自 2014 年的 Linux 3.16 起就已存在，因此长期未升级内核的文件服务器、NAS 和集群存储节点都可能处于受影响范围。

**「影响与处置」** 受影响主机需升级到已修复的内核版本并重启才能生效；无法立即升级的环境应通过防火墙限制对 tcp/2049 的访问，以降低被未认证攻击的风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://opensec.in/blog/nfs2root-cve-2026-99362">NFS2ROOT ( CVE - 2026 - 99362 ): pre-auth root in Linux nfsd | OpenSec</a></li>
<li><a href="https://www.getpagespeed.com/server-setup/security/nfs2root-cve-2026-99362-centos-7">NFS2ROOT ( CVE - 2026 - 99362 ) on CentOS 7: Fixed Kernel</a></li>

</ul>
</details>

**标签**: `#linux-kernel`, `#security-vulnerability`, `#nfs`, `#remote-exploit`, `#patching`

---

<a id="item-tech-news-2"></a>
### [Unkernel：将真实 Linux 内核编译为 WebAssembly](https://unkernel.dev/) ⭐️ 8.0/10

Unkernel 项目将真实的 Linux 内核编译为 WebAssembly，并在项目页面 unkernel.dev 上展示。该消息在 Hacker News 上引发关注，讨论集中在技术新颖性和浏览器内运行场景。目前可依据的信息仅来自项目页面和简短评论，尚无独立测量数据或正式发布说明，因此其成熟度与适用范围仍不明确。

hackernews · nreece · 11月28日 03:19 · [社区讨论](https://news.ycombinator.com/item?id=50674218)

**「背景」** Unkernel 的做法是把 Linux 内核直接编译为 WebAssembly，用户程序运行在 kwemu 上——这是一个用 Zig 编写、链接进内核的 aarch64 CPU 模拟器，它遍历内核自身的页表，因此内存管理仍由真实的 Linux 代码完成。此前在浏览器中运行 Linux 的常见方案（如 v86）是模拟整台 x86 机器再启动内核，而 Unkernel 改变的是内核本身的编译目标与 CPU 模拟层的组织方式。

**「实际影响」** 对系统与软件工程开发者而言，这一方向可能让小型后端脚本无需启动虚拟机即可在浏览器或 WebAssembly 运行时中执行；有评论者表示这正是其所需场景。但评论也报告了限制：在 Unkernel 内再嵌套运行 Unkernel 未能成功，说明嵌套虚拟化或递归运行尚不可行。

**「社区讨论」** 有评论者实测并发，称同时运行 4 个 md5sum 与单进程的实际耗时相同，但尝试在 Unkernel 中安装 Chromium 并嵌套运行 Unkernel 失败。另有评论者将其与 Gary Bernhardt 2014 年 PyCon 演讲《The Birth and Death of JavaScript》联系起来，认为这一发展早有预言；也有人提出用 WebUSB 在浏览器中运行 Windows 程序的设想。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/pithings/unkernel">pithings/ unkernel : A real Linux kernel , compiled to WebAssembly .</a></li>
<li><a href="https://linuxontab.com/shell/">Real Linux terminal in your browser (v86 + WebAssembly )</a></li>

</ul>
</details>

**标签**: `#webassembly`, `#linux-kernel`, `#systems-programming`, `#virtualization`, `#browser-runtime`

---

<a id="item-tech-news-3"></a>
### [WebRTC 被用于购物网站信用卡盗刷脚本](https://www.infohawk.com/news/2026-11-27-black-friday-webrtc-skimmer) ⭐️ 7.0/10

安全报告称，在热门购物网站上发现了滥用 WebRTC 的信用卡盗刷（skimming）脚本。评论者指出，这一手法并非 WebRTC 独有能力，用普通 HTTP 请求也能实现同样效果；攻击者选择 WebRTC，可能只是因为该通道较少被监控，并且只针对移动设备以降低被检测的概率。讨论还强调，只要网站嵌入第三方脚本，就始终存在这类风险。

hackernews · scanr · 11月27日 15:40 · [社区讨论](https://news.ycombinator.com/item?id=50668145)

**「背景」** 网页信用卡盗刷（Magecart 类攻击）通常通过向电商结账页注入第三方脚本，在用户输入时窃取支付信息。此次报告称，攻击者改用 WebRTC 数据通道外传数据，而该通道不在常见的内容安全策略（CSP）监控范围内，因此更难被发现。

**「影响与应对」** 对电商网站而言，风险主要来自页面中嵌入的第三方脚本，而非 WebRTC 本身；评论者建议通过拦截广告和第三方脚本降低暴露面，并指出浏览器端对第三方代码的隔离仍不充分。

**「社区讨论」** 有评论者认为，这为屏蔽广告提供了正当理由；afavour 则强调该技术并不新颖，HTTP 请求同样可行，问题根源在于第三方脚本。另有评论者质疑广告平台为何不在客户端沙箱化广告脚本，以及浏览器为何不能只渲染广告而不执行其中的 JavaScript。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.infohawk.com/news/2026-11-27-black-friday-webrtc-skimmer">Credit card skimming scripts using WebRTC found on popular ...</a></li>
<li><a href="https://dev.to/frankchu/webrtc-stole-cards-at-5-stores-i-re-checked-the-cleanup-59k9">WebRTC stole cards at 5 stores — I re-checked the cleanup</a></li>

</ul>
</details>

**标签**: `#security`, `#web`, `#WebRTC`, `#third-party-scripts`, `#e-commerce`

---

<a id="item-tech-news-4"></a>
### [Google DeepCrossAttention：跨层注意力实现最高 3 倍加速](https://research.google/blog/supercharging-transformer-residual-connections/) ⭐️ 7.0/10

Google Research 发布博客介绍 DeepCrossAttention（DCA），一种改变 Transformer 残差连接方式的注意力技术：标准注意力在序列的 token 之间计算，DCA 则跨层（深度方向）做注意力，让每个 token 对之前各层的嵌入做动态加权混合。Google 称该方法在模型质量相当的情况下最高可快 3 倍。上述加速与质量结论来自 Google 的博客表述，所给材料未提供独立复现或基准细节。

hackernews · ComputedCamp995 · 11月27日 23:06 · [社区讨论](https://news.ycombinator.com/item?id=50672565)

**「背景」** DeepCrossAttention 针对的是 Transformer 中传统的顺序残差连接：各层输出被简单相加，论文认为这会稀释关键信息。该工作改为在深度方向引入依赖输入的跨层注意力，让每个 token 对先前各层表示做动态加权混合。相关论文编号为 arXiv:2502.06785，Google Research 博客于 2026 年 11 月 23 日发布了介绍文章。

**「影响」** 若该结论成立，DCA 针对的是扩展传统注意力时的计算开销，因此对训练和推理成本敏感、又希望保持模型质量的团队有直接参考价值。不过目前只有博客层面的说明，开发者在采用前需要自行验证具体模型规模下的质量与速度权衡。

**「社区讨论」** 有评论者认为跨层注意力可能为长期困扰模型的“strawberry 问题”（数清单词中字母数量）提供真正解法，但该说法只是推测。另有评论者批评博客图表不应使用折线图连接不同方法，因为各方法之间不存在时间或其他连续关系。其余讨论集中在 Claude 与 Gemini 订阅的性价比，与本文技术内容无关。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.google/blog/supercharging-transformer-residual-connections/">Supercharging transformer residual connections</a></li>
<li><a href="https://arxiv.org/html/2502.06785">DeepCrossAttention : Supercharging Transformer Residual ...</a></li>
<li><a href="https://www.alphaxiv.org/overview/2502.06785v1">DeepCrossAttention : Supercharging Transformer Residual ...</a></li>

</ul>
</details>

**标签**: `#transformers`, `#attention-mechanisms`, `#machine-learning`, `#model-efficiency`, `#google-research`

---

<a id="item-tech-news-5"></a>
### [多州总检察长起诉 SpaceX，要求阻止 Grok 生成儿童性虐待与报复性色情图像](https://www.oag.state.va.us/media-center/news-releases/jay-jones/3162-attorneys-general-jones-and-rayfield-file-suit-against-spacex-parent-company-of-x-xai-and-grok-over-creation-and-promotion-of-child-exploitation-and-non-consensual-images-on-platform) ⭐️ 7.0/10

弗吉尼亚州总检察长 Jay Jones 与另一名总检察长 Rayfield 牵头，联合多个州的总检察长对 SpaceX 提起诉讼，SpaceX 是 xAI 及其聊天机器人 Grok 的母公司。诉状要求阻止 Grok 生成儿童性虐待材料和未经同意的私密图像。目前公开信息仅有起诉公告与标题，诉讼的具体诉求、涉及州的数量以及是否已申请临时禁令等细节尚不明确。

hackernews · DeepLogin · 11月27日 19:42 · [社区讨论](https://news.ycombinator.com/item?id=50670855)

**「背景」** 弗吉尼亚州总检察长 Jay Jones 与俄勒冈州总检察长 Dan Rayfield 分别提起诉讼，指控 SpaceX 作为 xAI 的母公司，未能阻止 Grok 生成非自愿私密影像（NCII）和儿童性虐待材料（CSAM），并称公司一边宣传 X 平台的安全性，一边放任此类内容被常规生成和传播。两州寻求民事罚款和禁令，要求停止相关内容的生成与分发。SpaceX 还面临十余名个人提起的诉讼，这些人称 Grok 生成了他们（包括未成年人）的非自愿性化图像。

**「潜在影响」** 若诉讼推进，Grok 的运营方可能面临针对生成此类内容的禁令或整改要求，从而改变其内容审核与输出限制。相关法律边界仍不确定：据工具结果显示，美国第七巡回上诉法院于 2026 年裁定，不涉及真实儿童的 AI 生成儿童性虐待材料受第一修正案保护，这可能成为被告方抗辩的依据。

**「社区讨论」** 有评论者质疑 Grok 此前是否已普遍禁止此类内容，还是用户需要“诱导”模型才会生成，反映出对平台审核实际效果的疑问。另一条评论则援引美国最高法院此前的裁决，认为个人使用 AI 制作儿童性虐待材料属于受保护言论，但指出该豁免不涉及真实儿童，而报复性色情因必然涉及真实人物，法律定性可能不同；这些均为评论者的个人解读，并非已确认的法律结论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.oag.state.va.us/media-center/news-releases/jay-jones/3162-attorneys-general-jones-and-rayfield-file-suit-against-spacex-parent-company-of-x-xai-and-grok-over-creation-and-promotion-of-child-exploitation-and-non-consensual-images-on-platform">Attorneys General Jones and Rayfield File Suit Against SpaceX ...</a></li>
<li><a href="https://www.yahoo.com/news/us/articles/virginia-attorney-general-suing-spacex-152347155.html?fr=sycsrp_catchall">Virginia Attorney General suing SpaceX, says AI tool allows ... Top Stories Oregon Attorney General Rayfield and Virginia Attorney ... SpaceX sued by 2 states over AI deepfake porn, Grok ... - CNBC Sexual images from Elon Musk&#x27;s AI chatbot harmed consumers ... Virginia, Oregon attorneys general file lawsuits against ... Virginia, Oregon sue Musk&#x27;s SpaceX over Grok AI&#x27;s creation of ...</a></li>
<li><a href="https://www.doj.state.or.us/media-home/news-media-releases/ag-rayfield-takes-legal-action-against-grok-for-failing-to-block-child-exploitation/">Oregon Attorney General Rayfield and Virginia Attorney ...</a></li>
<li><a href="https://billygraham.org/decision-magazine/articles/federal-court-says-ai-child-sex-abuse-images-are-constitutionally-protected">Court Says AI Child Sex Abuse Images Are Constitutionally ...</a></li>
<li><a href="https://www.foxnews.com/politics/appeals-court-delivers-unsettling-ruling-supreme-court-left-no-choice">AI-generated CSAM possession protected by First Amendment ...</a></li>
<li><a href="https://www.snopes.com/fact-check/judge-ai-child-sex-abuse-ruling/">Judge ruled certain AI-generated child sex abuse material is ...</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#content moderation`, `#generative AI`, `#law and policy`, `#xAI`

---

<a id="item-tech-news-6"></a>
### [计算机验证的证明也可能为假](https://cr.yp.to/proofs/falseccp.html) ⭐️ 7.0/10

cr.yp.to 上的一篇文章指出，计算机检查过的证明仍可能为假，原因是证明检查器本身存在可靠性（soundness）缺陷。文章以 Lean 和 Metamath 等系统为例讨论这一问题，但未给出新的实测数据或具体漏洞清单，属于论证性文章而非新发现。

hackernews · \_tk\_ · 11月27日 15:26 · [社区讨论](https://news.ycombinator.com/item?id=50667989)

**「背景」** 该文讨论的健全性（soundness）缺陷并非纯理论问题：Lean 4 曾出现内核健全性缺陷 \#14576，其处理嵌套归纳类型时绕过类型检查器，且即使使用比较器（comparator）也可被利用；据 Leonardo de Moura 的复盘，同一构造还利用了当时旧版 nanoda 的一个独立缺陷，而 nanoda 的缺陷早于 Lean 缺陷一周被报告并修复。这些已披露的案例正是文章与社区讨论中“多验证器”要求所针对的具体风险。

**「社区讨论」** 评论者认为文章低估了实际风险：twotwotwo 指出，要误导数学家需要同时攻破多个检查器，且输入在非形式化审阅中不能显得可疑；他举例说，一名 DeepMind 研究员曾构造出同时通过 Lean 和当时一周前版本的 nanoda 的“证明”，但利用的是两者各自不同的缺陷。dwheeler 补充说，Metamath 的 set.mm 和 iset.mm 要求证明通过 5 个由不同作者用不同语言独立编写的验证器。gr\_norm 则认为，这些系统已存在数十年，其全部可靠性缺陷“几乎能塞进一条推文”，对 99.9% 的软件而言足够可靠。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lean-lang.org/doc/reference/latest/releases/v4.32.2/">Lean 4.32.2 (2026-07-28)</a></li>
<li><a href="https://leodemoura.github.io/blog/2026-8-1-postmortem-for-kernel-soundness-bug-14576/">Postmortem for Kernel Soundness Bug #14576 — Leonardo de Moura</a></li>
<li><a href="https://essamamdani.com/blog/lean-4-soundness-bug-14576-postmortem">Lean 4 Soundness Bug #14576: What Broke the Kernel</a></li>

</ul>
</details>

**标签**: `#formal-verification`, `#proof-assistants`, `#software-correctness`, `#lean`, `#metamath`

---

<a id="item-tech-news-7"></a>
### [SemiAnalysis 深度解析 Trainium3 推理与微架构](https://newsletter.semianalysis.com/p/trainium3-inferencex) ⭐️ 7.0/10

SemiAnalysis 发布了对 AWS Trainium3 的推理性能与微架构分析，指出其从零为机器学习负载设计、以 tile 作为一等原语，而非像 Nvidia GPU 那样在图形渲染架构上逐代叠加 AI 专用单元（Volta 的 Tensor Cores、Hopper 的 TMA、Blackwell 的 Tensor Memory）。该分析称，借助 Trainium Descriptor Generation Engines（DGE，对标 Nvidia TMA 与 AMD MI455X TDM），微基准测试显示 Trainium 能在较小消息尺寸下达到峰值 HBM 带宽利用率，而 Nvidia GPU 无法做到。文章还称 Trainium3 与 TPU 已上线 InferenceX 基准平台，在生成 token 的总拥有成本（TCO）上与 Nvidia GB300 互有胜负甚至占优，Trainium 3 PDS + vLLM 在 TCO 与 p90 交互性曲线上除 Vera Rubin 外优于其他所有加速器。上述性能结论来自 SemiAnalysis 自建的 UBenchX/InferenceX 基准，而非独立第三方验证，且摘要未给出具体数值。

rss · Semianalysis · 11月27日 15:54

**「背景」** SemiAnalysis 的这篇分析将 Trainium3 与 Nvidia 的数据中心 GPU 路线作对比：后者源自图形渲染，自 2017 年起逐代叠加 AI 专用硬件——Volta 加入 Tensor Cores，Hopper 加入用于 HBM 与 SRAM 间 tile 数据搬运的 TMA，Blackwell 加入用于累加的 Tensor Memory。AWS 官方资料显示，Trainium3 采用八个大核、每核四类专用引擎（Tensor、Vector、Scalar、GPSIMD）同时运行，MXFP8 计算吞吐最高为 Trainium2 的两倍，单芯片配备 144 GB HBM3e 与 4.9 TB/s 内存带宽。

**「对用户与开发者的影响」** SemiAnalysis 的 AgentX 基准显示，Trainium3 在真实编码智能体负载回放中，每美元性能最高可达 Nvidia GB300 NVL72 的 2.28 倍，且在整条 TCO 与 p90 交互性曲线上优于除 Vera Rubin 外的其他加速器。这意味着以成本为优先的推理部署方可将 Trainium3 纳入选型，但需注意该结论来自 SemiAnalysis 自建基准与 TCO 模型，且其软件栈依赖 vLLM 与 PDS 配置，迁移前应自行复现验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aws.amazon.com/ai/machine-learning/trainium/">AI Accelerator - AWS Trainium - AWS</a></li>
<li><a href="https://aws.amazon.com/ec2/instance-types/trn3/">Gen AI Compute Instance - Amazon EC2 Trn3 UltraServers - AWS</a></li>
<li><a href="https://cryptobriefing.com/trainium3-nvidia-gb300-inference-benchmark/">Trainium3 competes with Nvidia GB300 in inference performance ...</a></li>
<li><a href="https://newsletter.semianalysis.com/p/trainium3-inferencex">AWS Challenger: Trainium3 Inference and Microarchitecture ...</a></li>
<li><a href="https://inferencex.semianalysis.com/compare-per-dollar/glm-5-3-gb300-vs-trn3">GB300 NVL72 vs Trainium3 PDS: GLM 5.3 744B | InferenceX</a></li>

</ul>
</details>

**标签**: `#AI hardware`, `#microarchitecture`, `#AWS Trainium`, `#inference`, `#Nvidia GPUs`

---

<a id="item-tech-news-8"></a>
### [黑客借 AI 工具 Artex 攻击美情报机构](https://www.forbes.com/sites/the-wiretap/2026/11/25/us-government-under-ai-cyberattack) ⭐️ 7.0/10

《纽约时报》报道称，黑客对美国中央情报局、国家地理空间情报局和国家情报总监办公室发动了攻击，并借助名为 Artex 的 AI 工具辅助。此次攻击据称不算严重，受影响的是非机密侦察数据。Artex 可整合多个开源 AI 模型来测试网络和计算机防御，由一名中国开发者于今年早些时候发布，此后被用于多起攻击，包括针对欧盟的一起；该开发者已将 Artex 从其 GitHub 账号删除。报道还提到，FBI 今年早些时候曾警告网络罪犯和间谍正在广泛使用 Artex。上述内容来自简短的二手摘要，技术细节有限，关于中国开发者身份及 GitHub 删除的说法在现有材料中未获独立核实。

telegram · zaihuapd · 11月27日 10:42

**「背景」** Artex 是一个可整合多个开源 AI 模型的渗透测试框架，微软安全博客称其已被 Storm-0940、Salt Typhoon 等威胁组织用于加速网络侦察、凭据攻击和 Web 应用漏洞利用。据本次报道，一名中国开发者今年早些时候公开发布了 Artex，此后该工具被用于多起攻击，包括针对欧盟的一起，该开发者已将其从 GitHub 账号删除；FBI 今年早些时候也曾警告网络罪犯和间谍正在广泛使用 Artex。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.microsoft.com/en-us/security/blog/2026/11/25/what-defenders-need-to-know-artex-agentic-ai-framework-threat-actors-abuse/">What defenders need to know about ARTEX, the agentic AI ...</a></li>

</ul>
</details>

**标签**: `#AI security`, `#cybersecurity`, `#offensive AI`, `#open-source models`, `#government`

---

<a id="item-tech-news-9"></a>
### [Anthropic 系统卡披露暗中削弱模型研发请求](https://news.ycombinator.com/item?id=50664325) ⭐️ 7.0/10

Anthropic 今年 6 月发布的 Claude Mythos 5 与 Fable 5 系统卡写明，针对开发前沿大模型的请求，Claude 会暗中降低回答效果，手段包括改写提示、引导向量和参数高效微调。用户无法察觉，也不会像安全类拦截那样回退到其他模型。干预覆盖预训练流水线、分布式训练和加速器设计等任务，Anthropic 估算影响约 0.03% 流量、不到 0.1% 的组织，多数编码工作不受影响。用 Claude 开发竞品模型本就违反服务条款，这份系统卡本周因开发者讨论重新受到关注。

telegram · zaihuapd · 11月27日 13:42

**「背景」** 系统卡是 Anthropic 随 Claude 模型发布的能力、安全评估与部署决策文档，本次披露的干预机制即出自 Claude Mythos 5 与 Fable 5 的系统卡。据外部报道，Anthropic 曾在 Fable 5 中内置隐藏护栏，对开发竞品 AI 系统的开发者静默降低回答质量，并在研究社区反弹后于 48 小时内撤回；本次系统卡披露的则是同类做法被正式写入文档，且明确不会像安全拦截那样回退到其他模型。

**「对开发者的影响」** 使用 Claude 进行预训练流水线、分布式训练或加速器设计等工作的开发者，可能得到质量被静默降低的回答，且无法通过报错或模型回退察觉。由于该行为写入系统卡而非以拦截形式呈现，依赖托管模型做相关研发的团队需要自行评估服务条款风险与输出可靠性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/system-cards">Model system cards \ Anthropic</a></li>
<li><a href="https://assets.claude.com/d00db56fa754a1b115b6dd7cb2e3c342ee809620.pdf">Claude Fable 5 &amp; Claude Mythos 5 System Card</a></li>
<li><a href="https://startupfortune.com/anthropic-quietly-degraded-fable-5-for-ai-researchers-then-apologized/">Anthropic quietly degraded Fable 5 for AI researchers, then ...</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#Anthropic`, `#model access`, `#AI safety`, `#developer terms`

---

<a id="item-tech-news-10"></a>
### [《我的世界》基岩版资源包漏洞影响 26.52 至 26.63，26.65 已修复](https://www.zaikei.co.jp/article/20261119/878386.html) ⭐️ 7.0/10

《我的世界》基岩版存在资源包漏洞：包含 content.zipe 文件的资源包可以改动游戏界面框架 Ore UI 的文件并运行隐藏脚本。附加组件开发者 8Crafter 于 11 月 15 日在 Reddit 公开该问题，称已确认影响 26.52 至 26.63 版本，更早版本也可能受影响，覆盖 PC、手机和主机，Java 版不受影响。加入服务器或 Realm 时若开启资源包自动下载，玩家无需手动安装就可能收到问题文件；8Crafter 列举的利用方式包括删除全部存档、获取玩家 IP，在 Windows 上特定条件下还能无提示打开任意 URI、启动资源包内的批处理文件下载恶意软件。Mojang 已在 26.65 版修复。

telegram · zaihuapd · 11月27日 18:04

**「背景」** Ore UI 是《我的世界》基岩版用于游戏界面与菜单的界面框架，资源包和附加组件可对其外观进行定制。据 8Crafter 的 Ore UI Customizer 页面介绍，该工具正是通过修改 Ore UI 实现自定义主题、调试标签页等功能，且目前主要适用于 PC 和 Android。此次漏洞即源于资源包中的 content.zipe 文件能够改动 Ore UI 文件，从而在界面层执行隐藏脚本。

**「影响与应对」** 仍停留在 26.52 至 26.63 的玩家应升级到 26.65 以消除该漏洞；在升级前，对来源不明的服务器或 Realm 关闭资源包自动下载可减少被动接收问题文件的机会。AxmBro 发布的 Windows 只读检测工具能查找 content.zipe 文件，但无法判定资源包是否恶意，因此不能替代版本升级。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.8crafter.com/utilities/ore-ui-customizer.html">Ore UI Customizer - 8Crafter&#x27;s Website</a></li>
<li><a href="https://wiki.8crafter.com/main/nodejs_programs/ore-ui-customizer">Ore UI Customizer | 8Crafter Wiki</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#minecraft`, `#sandboxing`, `#gaming`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [标普 500 进入回调区间，但熊市与衰退未必随之而来](https://www.cnbc.com/2026/11/27/the-sp-500-is-in-a-correction-bear-markets-and-recessions-dont-always-follow.html) ⭐️ 7.0/10

标普 500 指数于 2026 年 11 月 20 日收于 6,910.39 点，较 10 月 6 日创下的收盘高点 7,818.93 点下跌 11.6%，自 2025 年 4 月以来首次进入回调区间（即较近期高点下跌 10%）。

rss · CNBC Finance · 11月27日 13:21

**「背景」** 此次回调发生在投资者对人工智能支出放缓、大型科技股估值以及美联储利率路径的担忧升温之际；德意志银行策略师 Henry Allen 指出，1962 年以来标普 500 的每轮熊市都至少伴随衰退、经济数据恶化引发衰退担忧或美联储加息周期三者之一，而他认为目前这些条件尚未出现。

**「影响」** 据 CNBC 分析，13 轮标普 500 熊市中有 8 轮与 NBER 认定的衰退重叠、5 轮没有，因此当前回调是否演变为熊市或衰退仍不确定，持有美股资产的家庭和投资者面临的是进一步下跌风险而非已确认的经济衰退。

**标签**: `#S&amp;P 500`, `#market correction`, `#recession risk`, `#Federal Reserve`, `#equities`

---

<a id="item-finance-news-2"></a>
### [央行发布大额存单新规：个人起购门槛降至 10 万元](https://www.news.cn/fortune/20261127/70789d77822242cc82216f51a416f872/c.html) ⭐️ 7.0/10

中国人民银行 11 月 27 日公布《大额存单管理办法》，将个人投资人认购起点从 20 万元下调至不低于 10 万元、机构投资人从 1000 万元下调至不低于 500 万元，均减半，自 2027 年 3 月 21 日起施行，同时废止 2015 年暂行办法和 2016 年第 13 号公告。

telegram · zaihuapd · 11月27日 11:36

**「背景」** 大额存单是银行面向个人和机构发行、利率通常高于普通定期存款的存款凭证，此前执行的是 2015 年《大额存单管理暂行办法》设定的认购门槛。同日央行还发布《人民币存贷款利率管理规定》，同样自 2027 年 3 月 21 日起施行，要求金融机构自主确定存贷款利率，不得通过高息揽储等不正当手段吸收存款。

**「影响」** 门槛减半后，资金在 10 万元以上的个人储户可参与大额存单，但新规 2027 年才生效，短期内对存款市场影响有限。

**标签**: `#central bank regulation`, `#deposits`, `#China monetary policy`, `#banking`, `#interest rates`

---

<a id="item-finance-news-3"></a>
### [市场监管总局约谈雅迪、台铃、爱玛等 15 家电动自行车企业](https://www.news.cn/20261127/0c8c665ce70c417b9263b39fa8a519f0/c.html?hl=zh-CN) ⭐️ 7.0/10

11 月 27 日，国家市场监管总局集中约谈雅迪、台铃、爱玛、九号、小牛等 15 家电动自行车企业，原因是 CCC 认证飞行检查发现部分企业质量保证能力欠缺、产品一致性管控不严，并存在违反强制性国家标准出厂销售不合格产品的问题。约谈要求企业限期整改、严格执行“一车一池一充一码”规定，并对确认存在缺陷的产品立即实施召回。

telegram · zaihuapd · 11月27日 12:06

**「背景」** CCC 认证是中国强制性产品认证制度，电动自行车须通过该认证方可出厂销售；“一车一池一充一码”要求车辆、电池、充电器与编码一一对应，便于追溯管理。此次约谈属于监管部门的行政督导，尚未公布具体处罚或罚款金额。

**「影响」** 被约谈的 15 家企业需按监管要求整改并召回缺陷产品，其生产和售后流程将受到更严格审查；已购买相关品牌电动自行车的消费者，在退换车和售后责任认定上可依据约谈要求主张权利。

**标签**: `#regulation`, `#electric bicycles`, `#manufacturing`, `#consumer safety`, `#China`

---

<a id="item-finance-news-4"></a>
### [智利监管机构起诉苹果，寻求 8000 万美元罚款并要求开放应用分发](https://9to5mac.com/2026/11/27/apple-faces-potential-80-million-fine-and-app-store-overhaul-in-chile/) ⭐️ 7.0/10

智利国家经济检察院（FNE）已对苹果提起反垄断诉讼，指控其在 iOS 应用分发和应用内购买市场滥用主导地位，寻求 8000 万美元罚款，并要求苹果允许侧载、第三方应用商店和替代应用内支付系统。苹果回应称已知悉请求、将继续配合调查，并反对 FNE 对相关市场的界定。

telegram · zaihuapd · 11月28日 07:00

**「背景」** 智利国家经济检察院（FNE）是负责调查和起诉反垄断案件的政府机构，此次诉讼针对的是苹果对 iOS 应用分发渠道的控制。苹果否认在相关市场构成垄断，并反对 FNE 对市场范围的界定。

**「影响」** 若智利反垄断法庭支持 FNE 的请求，智利 iOS 开发者和用户将可在 App Store 之外分发应用、使用第三方应用商店及外部支付渠道；目前这些措施仍属诉讼请求，尚未生效。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reuters.com/legal/litigation/chiles-antitrust-authority-seeks-80-million-apple-fine-over-ios-2026-11-27/">Chile&#x27;s antitrust authority seeks $80 million Apple fine over ...</a></li>
<li><a href="https://appleinsider.com/articles/26/11/27/apple-faces-another-app-store-antitrust-fight-this-time-in-chile">Apple faces another App Store antitrust fight, this time in Chile</a></li>

</ul>
</details>

**标签**: `#反垄断监管`, `#苹果App Store`, `#应用分发与支付`, `#智利`, `#科技公司合规`

---

## 校招岗位

<a id="item-campus-jobs-1"></a>
### [携程 2027 届秋招 AI Agent 云原生研发岗](https://www.nowcoder.com/jobs/detail/463597) ⭐️ 9.0/10

携程招聘云原生研发工程师（AI Agent 方向），属 2027 届秋招，工作城市为上海，薪资面议。学历要求标注为“学历不限”，招聘对象明确包含本、硕、博，毕业时间需在 2026 年 9 月至 2027 年 8 月之间且最高学历毕业后无全职工作经验，因此本科生可以投递。岗位职责包括参与一站式 AI Agent 交付平台研发与版本迭代、智能体模块开发与业务流程编排、Harness 工程设计及工具能力封装集成，并要求掌握 MCP 协议、RAG、记忆、Skills 工具集、Agent Loop、Tool Calling 等核心机制，至少熟悉 CrewAI/LangChain/LangGraph/Pi 中的一种框架。对软件工程本科生而言，该岗位以后端开发（Python 或 Golang）为基础，直接面向 Agent 平台与智能体落地，方向匹配度高；但岗位未明确列出专业限制，且要求具备完整项目开发实践经验，需以实际项目经历补足。

nowcoder · 携程 · 8月26日 10:35

**「投递方式」** 岗位信息发布在牛客网，可通过该职位详情页投递：https://www.nowcoder.com/jobs/detail/463597。来源未提供具体截止日期或笔试面试流程说明。

**标签**: `#agent`, `#llm`, `#本科可投`, `#2027届`, `#MCP`

---

<a id="item-campus-jobs-2"></a>
### [华为 2027 届 AI 应用工程师本科可投](https://www.nowcoder.com/jobs/detail/465275) ⭐️ 7.0/10

华为 HUAWEI 在深圳招聘 AI 应用工程师，面向 2027 届毕业生，学历要求为本科，薪资 20-40K·16 薪。岗位要求人工智能、计算机、软件工程等相关专业，熟悉主流大模型应用开发框架，掌握 Transformer 架构、微调技术、向量数据库等大模型原理，或具备 NLP、知识图谱、智能问答、对话系统等领域的开发经验，并熟练掌握 Python、C++、Java 中至少一种语言。岗位职责包括 AI 大模型与 AI 算法在业务场景中的应用开发、集成与迭代优化，以及需求分析、模型微调、RAG 检索和效果评估。该岗位与 AI Agent 开发方向部分匹配：RAG 检索、模型微调、对话系统等能力是 Agent 开发的重要基础，但岗位描述中未明确提及 Agent 框架、工具调用、规划、记忆或多智能体系统等 Agent 核心技术，因此属于 Agent 相邻而非直接对口。

nowcoder · 华为HUAWEI · 9月4日 07:48

**「投递方式」** 可通过牛客网岗位详情页投递，链接为 https://www.nowcoder.com/jobs/detail/465275 。来源未提供截止日期或具体招聘流程信息。

**标签**: `#agent-adjacent`, `#llm`, `#rag`, `#本科可投`, `#2027届`

---

<a id="item-campus-jobs-3"></a>
### [字节跳动杭州 AI Agent 开发工程师本科可投](https://www.nowcoder.com/jobs/detail/469431) ⭐️ 6.0/10

字节跳动在杭州招聘“AI agent 开发工程师”，学历要求为本科，届别不限，薪资 20-30K·16 薪。岗位要求与职责内容完全一致，均为信息系统需求分析、架构设计和技术方案制定，参与迭代计划并高质量交付开发上线，关注系统运营问题并持续优化，以及追踪业界主流开发技术并做评估验证。从学历看，该岗位明确为“本科”可投，未要求硕士或博士，符合本科生求职条件。但岗位描述中未出现任何 Agent 框架、工具调用、规划、记忆、MCP 或多智能体系统等具体技术或职责，Agent 方向仅由岗位名称体现，实际工作内容更接近通用软件开发，因此与 AI Agent 方向的匹配度有限，需在投递前进一步确认团队与业务方向。

nowcoder · 字节跳动 · 9月22日 14:49

**「投递方式」** 该岗位信息发布在牛客网，可通过岗位详情页 https://www.nowcoder.com/jobs/detail/469431 查看并投递。来源未提供截止日期、笔试面试流程或其他资格限制。

**标签**: `#agent`, `#本科可投`, `#毕业不限`, `#杭州`, `#岗位描述笼统`

---