---
layout: default
title: "Horizon Summary: 2026-11-26 (ZH)"
date: 2026-11-26
lang: zh
---

> 从 41 条内容中筛选出 13 条重要资讯。

---

**科技新闻**
1. [1Password 披露 2026 年 11 月安全事件：恶意代码被推入后端服务](#item-tech-news-1) ⭐️ 8.0/10
2. [Google 发布 Cogentic 整数分解与离散对数研究论文](#item-tech-news-2) ⭐️ 8.0/10
3. [Minecraft Java 版曝高危 RCE 漏洞，暂无官方补丁](#item-tech-news-3) ⭐️ 8.0/10
4. [FCC 批准 SpaceX 部署最多 100 万颗 Starmind 数据中心卫星](#item-tech-news-4) ⭐️ 8.0/10
5. [华为拟公布新款 HBM 芯片，论文称数据引脚密度翻倍](#item-tech-news-5) ⭐️ 8.0/10
6. [Neuralink 获 FDA 批准启动渐冻症关键临床试验](#item-tech-news-6) ⭐️ 8.0/10
7. [GRH 证明的 Lean 形式化被压缩至约 7.6 万行](#item-tech-news-7) ⭐️ 7.0/10
8. [预印本称多项式 Hirsch 猜想被证伪](#item-tech-news-8) ⭐️ 7.0/10
9. [SemiAnalysis 推出 GDPx 基准，评测前沿模型](#item-tech-news-9) ⭐️ 7.0/10
10. [三星与 SK 海力士据报交叉许可采用长江存储 Xtacking 技术](#item-tech-news-10) ⭐️ 7.0/10
11. [1Password 确认安全事件：员工 GitHub 账户被入侵](#item-tech-news-11) ⭐️ 7.0/10

**财经新闻**
1. [美商务部被曝施压英特尔交出 10%股权](#item-finance-news-1) ⭐️ 8.0/10
2. [美国拟对 14 个贸易伙伴加征第 301 条新关税](#item-finance-news-2) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [1Password 披露 2026 年 11 月安全事件：恶意代码被推入后端服务](https://1password.com/blog/update-on-nov-2026-security-incident) ⭐️ 8.0/10

1Password 于 2026 年 11 月 25 日发布博客，披露一起 2026 年 11 月的安全事件：有恶意代码被推送到其后端服务。公告称受影响记录涉及少量用户，这些用户已被单独通知。目前公开信息未说明攻击者如何获得推送权限、是否启用了分支保护，也未明确说明用户加密保险库是否被下载。

hackernews · lxhrstn · 11月25日 17:18 · [社区讨论](https://news.ycombinator.com/item?id=50644817)

**「事件背景」** 1Password 于 2026 年 11 月 19 日开始调查迹象，发现一名员工的公司 GitHub 账户被入侵；攻击者利用该账户访问源代码，并向后端服务推送了恶意代码。这一时间线来自 1Password 官方博客的更新以及 MacRumors 的报道，说明事件起点是员工账户失陷，而非直接攻破生产基础设施。

**「影响与关注点」** 对使用 1Password 在线保险库的用户而言，关键待确认问题是加密保险库数据是否被访问，以及被推送的代码在生产环境中运行了多久。评论者指出，公告未说明是否缺少分支保护规则或规则是否被绕过，这直接关系到其他 SaaS 团队评估自身代码推送与部署权限的隔离措施。

**「社区讨论」** 安全从业者 tptacek 认为，员工笔记本被攻陷后攻击者借其权限向 GitHub 推送代码并部署，是 SaaS 公司最标准的入侵路径，且随员工规模增长几乎必然发生。ctidd 批评公告未说明是否禁用向主分支推送、是否缺少分支保护规则；ChrisHardie 表示自己长期只用本地保险库，担心此类事件最终演变为中间人攻击；fn-mote 则希望公司明确声明“加密保险库未被下载”。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://1password.com/blog/update-on-nov-2026-security-incident">Update on a security incident involving 1 Password ’s backend ...</a></li>
<li><a href="https://www.macrumors.com/2026/11/25/1password-security-breach/">1 Password Security Breach: What Was Accessed and... - MacRumors</a></li>

</ul>
</details>

**标签**: `#security`, `#supply-chain`, `#saas`, `#password-manager`, `#incident-response`

---

<a id="item-tech-news-2"></a>
### [Google 发布 Cogentic 整数分解与离散对数研究论文](https://github.com/google-research/google-research/tree/master/cogentic_research_papers) ⭐️ 8.0/10

Google 在 google-research 仓库中发布了名为 Cogentic 的研究论文集合，主题包括整数分解、离散对数及相关数论问题。目前可获取的信息仅为该 GitHub 目录链接，论文的具体算法、复杂度结论和是否经过同行评审均未在来源中说明，因此尚不能确认这是密码学意义上的突破。社区讨论指出，整数分解结果建立在通用数域筛法（GNFS）之上，并未证明 GNFS 依赖的三个启发式猜想，而是替换了其中依赖猜想的环节并承担了较大的复杂度代价。

hackernews · rgwohlbold · 11月25日 13:33 · [社区讨论](https://news.ycombinator.com/item?id=50642086)

**「背景」** 整数分解和离散对数都是公钥密码学的基础难题：RSA 的安全性依赖大整数分解的困难性，而许多其他密码协议则依赖离散对数问题。评论者 gukoff 指出，谷歌此次的整数分解结果建立在通用数域筛法（GNFS）之上，而 GNFS 本身依赖三个未经证明的启发式假设；Cogentic 并未证明这些假设，而是替换了依赖它们的那部分步骤，并为此付出了复杂度上的代价。

**「影响」** 对密码学从业者而言，当前证据不足以调整对 RSA 或离散对数类方案安全性的评估；在论文细节和独立验证出现前，应把该发布视为待审阅的研究材料，而非已确认的算法进展。

**「社区讨论」** 评论者 gukoff 认为该整数分解结果的形式有些出人意料：它基于渐近复杂度更好的 GNFS，但没有证明后者依赖的启发式猜想，而是替换相关部分并付出较大复杂度代价，因此结果有趣但门槛已被抬高。另有评论者 fidotron 提到，有可信人士传言这只是更大成果的开端，并附上一条 X 链接，但该说法未获证实。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Discrete_logarithm">Discrete logarithm - Wikipedia</a></li>
<li><a href="https://news.ycombinator.com/item?id=50642086">Google releases Cogentic papers on integer factorization , discrete ...</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#integer-factorization`, `#algorithms`, `#research`, `#number-theory`

---

<a id="item-tech-news-3"></a>
### [Minecraft Java 版曝高危 RCE 漏洞，暂无官方补丁](https://github.com/bikini/minecraft2shell) ⭐️ 8.0/10

11 月 22 日公开的 minecraft2shell 披露，Minecraft Java 版服务器资源包中的特制 TrueType 字体可触发 FreeType 2.14.3 及更早版本的原生越界写，从而在 Windows 客户端执行任意代码。受影响范围为 Java 版 1.20.5 至 1.21.10 以及 26.1 至 26.4 快照，1.20.4 及更早版本和基岩版不受影响。Mojang 目前仍使用 lwjgl-freetype 3.4.3，尚无官方补丁；社区于 11 月 24 日发布 m2sfix 1.0.0，通过 Java agent 或 mod 关闭 hinting 作为临时缓解。

telegram · zaihuapd · 11月25日 12:46

**「背景」** 该漏洞的根源在 Minecraft Java 版渲染资源包字体所依赖的 FreeType 库：特制 TrueType 字体可触发 FreeType 2.14.3 及更早版本的原生越界写，进而执行任意代码。据外部报道，Mojang 尚未发布基于 FreeType 2.15 的修复，公开利用自 11 月 22 日起在 26.3 版本上有效。

**「影响与应对」** 在官方修复发布前，玩家应避免添加任何资源包，并将多人游戏服务器的资源包权限设为“禁用”，或安装社区临时修复 mod。由于漏洞通过服务器下发的资源包触发，加入不受信任的服务器时风险尤其直接。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wurst.wiki/minecraft2shell">Minecraft2Shell Vulnerability - wurst.wiki</a></li>
<li><a href="https://minecraft.pl/en/news/minecraft2shell-unpatched-rce-vulnerability-in-minecraft-java">Minecraft2Shell: Unpatched RCE Vulnerability in Minecraft</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#minecraft`, `#freetype`, `#open-source`

---

<a id="item-tech-news-4"></a>
### [FCC 批准 SpaceX 部署最多 100 万颗 Starmind 数据中心卫星](https://www.geekwire.com/2026/fcc-clears-spacex-million-satellites-starmind-data-center/) ⭐️ 8.0/10

美国联邦通信委员会（FCC）批准 SpaceX 在 500 至 1002 公里高度部署最多 100 万颗卫星，用于构建 Starmind 在轨数据处理网络。FCC 称这是美国首次批准太空数据中心星座。授权附带通信备份、定期提交进展和轨道碎片减缓详细方案等条件：首颗卫星须不晚于 2033 年投入运行，整个星座须在 2040 年前全部运行。FCC 在审批中驳回了亚马逊、Viasat 和美国天文学会的反对意见。该消息经 Telegram 频道转述 GeekWire 报道，除上述条件外未提供更多技术或审批细节。

telegram · zaihuapd · 11月26日 04:45

**「背景」** FCC 此次授权针对的是 SpaceX 提出的 Starmind 在轨数据处理星座申请，该星座计划在 500 至 1002 公里高度运行，用于在太空提供数据中心能力。FCC 在批准文件中将其描述为支持美国“超级智能经济”的 Starmind 卫星网络，并称这是美国首次批准太空数据中心星座。

**「对运营与合规的影响」** 获批星座须在 2033 年前让首颗卫星投入运行、2040 年前全部部署完毕，并定期向 FCC 提交进展和轨道碎片减缓详细方案，这意味着 SpaceX 的部署节奏与退役处置将受到阶段性合规约束。此前已有分析指出，大规模在轨数据中心卫星再入可能影响高层大气化学并产生太空电子废弃物，相关处置要求因此成为该星座运营的关键条件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.fcc.gov/document/fcc-authorizes-1-million-satellites-data-centers-space-0">FCC Authorizes 1 Million Satellites for Data Centers in Space</a></li>
<li><a href="https://apnews.com/article/spacex-data-center-elon-musk-b9897fe06f851ffaf92fd304ae69075c">FCC says SpaceX can deploy 1 million satellites for data ...</a></li>
<li><a href="https://satnews.com/2026/08/20/orbital-data-center-constellations-face-scrutiny-over-atmospheric-re-entry-pollution-and-space-e-waste/">Orbital Data Center Constellations Face Scrutiny Over Atmospheric...</a></li>

</ul>
</details>

**标签**: `#space computing`, `#satellite internet`, `#FCC regulation`, `#SpaceX`, `#orbital debris`

---

<a id="item-tech-news-5"></a>
### [华为拟公布新款 HBM 芯片，论文称数据引脚密度翻倍](https://www.bloomberg.com/news/articles/2026-11-26/huawei-teases-next-gen-ai-memory-chip-to-take-on-samsung-hynix) ⭐️ 8.0/10

华为计划公布一款新型高带宽内存（HBM）芯片的细节，其研究论文标题显示，该芯片的数据引脚密度是三星电子和 SK 海力士量产产品的两倍，理论上可大幅提升内存带宽。华为计划于明年 2 月在旧金山的一场会议上发表这篇论文。华为同时正推动 HBM 在中国本土投产，而该部件目前受美国制裁限制。上述性能说法目前仅来自论文标题和会议计划，尚无独立测试或产品时间表。

telegram · zaihuapd · 11月26日 05:30

**「背景」** HBM（高带宽内存）通过堆叠多层 DRAM 并以更宽的数据接口提升带宽，长期由三星和 SK 海力士主导。据维基百科记载，两家公司在 2016 年 Hot Chips 会议上已各自公布新一代 HBM 技术，此后持续以增加密度、带宽并降低功耗为迭代方向。华为此次提出的数据引脚密度翻倍属于研究论文层面的设计主张，尚待明年 2 月会议披露细节及后续验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>

</ul>
</details>

**标签**: `#HBM`, `#Huawei`, `#semiconductor`, `#hardware`, `#AI memory`

---

<a id="item-tech-news-6"></a>
### [Neuralink 获 FDA 批准启动渐冻症关键临床试验](https://www.bloomberg.com/news/articles/2026-11-25/neuralink-gets-clearance-for-brain-implant-trial-in-als-patients?srnd=phx-technology) ⭐️ 8.0/10

Neuralink 宣布获得 FDA 批准，将在美国启动名为“LINK”的植入式脑机接口关键临床试验，面向渐冻症（ALS）患者招募，目标是把大脑信号直接转化为计算机控制指令。报道称这是美国首个获批的此类关键试验。此前该公司通过早期研究已在全球为超过 30 名瘫痪患者植入设备；此次进入关键临床阶段后，相关数据将作为未来申请医疗器械上市许可的核心依据。

telegram · zaihuapd · 11月26日 07:15

**「背景」** 关键临床试验（pivotal trial）是医疗器械在美国申请上市前通常需要完成的大规模有效性验证阶段，其数据将作为监管审批的核心依据。Neuralink 此前通过早期研究已在全球为超过 30 名瘫痪患者植入设备，此次获批意味着相关工作从安全性验证推进到面向上市审批的有效性验证阶段。

**「影响与关注点」** 对渐冻症患者而言，这项关键试验意味着植入式脑机接口从早期安全验证转向以上市审批为目标的疗效数据收集，但获批启动试验并不等于设备已获准上市，实际可用性仍取决于试验结果与后续审评。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://neuralink.com/updates/neuralink-receives-fda-approval-to-launch-link-pivotal-study/">Neuralink Receives FDA Approval to Launch LINK Pivotal Study</a></li>
<li><a href="https://www.neurapod.com/blog/neuralink-fda-approval-link-pivotal-trial">Neuralink Gets FDA Approval for LINK, Its First Pivotal Trial</a></li>
<li><a href="https://teslanorth.com/2026/11/25/neuralink-fda-link-pivotal-brain-implant-trial-als/">Neuralink Says FDA Cleared Its First Pivotal Brain Implant Trial</a></li>

</ul>
</details>

**标签**: `#brain-computer interface`, `#Neuralink`, `#FDA regulation`, `#neurotechnology`, `#clinical trials`

---

<a id="item-tech-news-7"></a>
### [GRH 证明的 Lean 形式化被压缩至约 7.6 万行](https://github.com/lsernau/grh-lean) ⭐️ 7.0/10

GitHub 仓库 lsernau/grh-lean 发布了一个更短、更易读的 GRH 证明 Lean 形式化版本。据社区评论，代码规模从约 1700 万行降至约 7.6 万行，并区分了“已知数学”与“新数学”部分，还配有面向人类阅读的文档。该仓库为链接形式，所给材料未提供独立验证，因此这些行数与可读性说法目前应视为仓库作者及评论者的陈述，而非已核实的结果。

hackernews · nb-t · 11月25日 21:48 · [社区讨论](https://news.ycombinator.com/item?id=50648050)

**「背景」** 据外部报道，Anthropic 的数学家 Levent Alpöge 借助 Claude 在约六周内产出了一份约 1740 万行 Lean 代码的黎曼猜想证明，多个独立检查器接受了该证明，但当时尚无人能解释其为何成立。此次仓库展示的是同一证明的压缩版本，行数从约 1700 万降至约 7.6 万，并附有可读文档与“已知数学/新数学”的区分。

**「对形式化数学阅读与验证的影响」** 该仓库把 GRH 证明的 Lean 形式化从约 1700 万行压缩到约 7.6 万行，并区分“已知数学”与“新数学”、补充人类可读文档，这直接回应了 Terence Tao 此前指出的自动形式化困境：AI 能生成正确但无人能读的证明，形成人类审阅瓶颈。不过社区评论者 delegate 以仓库中的具体代码为例质疑，即便行数大幅减少，非 Lean 专家仍难以判断人类能否真正读懂并验证其正确性；因此压缩规模是否等同于可审阅性，目前尚无独立验证。

**「社区讨论」** 有评论者认为，清晰的“已知数学/新数学”划分和文档有助于理解这份证明；也有人追问，这是否回应了陶哲轩此前关于“巨型证明缺乏洞见”的批评，以及更聪明的 LLM 能否通过精简证明并加以解释来绕过该问题。另有不熟悉 Lean 的读者贴出具体代码片段，质疑人类是否真能读懂并验证其正确性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Alp%C3%B6ge&#x27;s_proof_of_the_Riemann_hypothesis">Alpöge&#x27;s proof of the Riemann hypothesis - Wikipedia</a></li>
<li><a href="https://www.npr.org/2026/11/21/g-s1-154922/anthropic-worker-claims-to-have-solved-a-holy-grail-of-math-problems-with-the-help-of-ai">Anthropic worker claims to have solved a Holy Grail of math... : NPR</a></li>
<li><a href="https://www.youtube.com/watch?v=D5_IneLBKN0">I Read Both Riemann Hypothesis &quot; Proofs &quot; From the Same... - YouTube</a></li>
<li><a href="https://tangente-mag.com/en/articles/terence-tao-warns-ai-is-writing-proofs-that-no-one-can-read">Terence Tao warns: AI writes proofs no one can read</a></li>
<li><a href="https://www.researchgate.net/post/How_can_the_scientific_community_resolve_Terence_Taos_2026_Proof_Indigestion_crisis_in_automated_mathematics_and_AI_formalization">How can the scientific community resolve Terence Tao&#x27;s (2026 ...</a></li>

</ul>
</details>

**标签**: `#formal-verification`, `#Lean`, `#mathematics`, `#AI-assisted-proofs`, `#open-source`

---

<a id="item-tech-news-8"></a>
### [预印本称多项式 Hirsch 猜想被证伪](https://github.com/openai/math/blob/main/preprints/Superpolynomial-graph-diameter-of-simple-polytopes-November-24-2026/paper.pdf) ⭐️ 7.0/10

一份发布在 OpenAI GitHub 仓库中的预印本论文声称证伪了多项式 Hirsch 猜想。据社区评论解读，这意味着不存在多项式时间的单纯形算法，而单纯形法是求解线性规划的标准方法之一。该结果被评论者视为对 2010 年原始 Hirsch 猜想被证伪之后的“收尾工作”，而非全新的基础性突破。论文目前仅为预印本，尚未见同行评审或独立验证。

hackernews · acossta · 11月25日 17:34 · [社区讨论](https://news.ycombinator.com/item?id=50644980)

**「背景」** 多项式 Hirsch 猜想是原始 Hirsch 猜想的松弛版本：后者曾猜测 d 维、n 个面的多面体任意两顶点间最多只需 n−d 步，但该原始猜想在 2010 年被证伪，结束了它约 50 年的悬置状态。据 Wikipedia 条目，OpenAI 于 2026 年 11 月 24 日发布预印本，构造了面数 n 固定、维度次多项式增长且图直径增长快于 n 任意固定次幂的有界简单有理多面体，从而否定多项式 Hirsch 猜想。

**「影响」** 若结论成立，它从理论上排除了单纯形法在最坏情况下具有多项式时间复杂度的可能，但这与单纯形法在实践中表现良好并不矛盾，因此对日常线性规划求解器的使用影响有限。对算法研究者而言，该结果进一步界定了多面体图上顶点间最短路径长度的上界问题。

**「社区讨论」** 评论者 GIFtheory 指出，原始 Hirsch 猜想曾试图解释单纯形法为何在实践中表现出色，但该猜想早在 2010 年、历经 50 多年后被证伪，因此这次更像是“收尾”性质的结果。另有评论者用立方体图上的边数作类比，帮助理解多面体直径与 Hirsch 猜想的关系。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hirsch_conjecture">Hirsch conjecture - Wikipedia</a></li>

</ul>
</details>

**标签**: `#linear programming`, `#computational complexity`, `#simplex algorithm`, `#mathematics`, `#polytopes`

---

<a id="item-tech-news-9"></a>
### [SemiAnalysis 推出 GDPx 基准，评测前沿模型](https://newsletter.semianalysis.com/p/evaluating-recent-model-releases) ⭐️ 7.0/10

SemiAnalysis 于 11 月 1 日发布 GDPx 基准，用于衡量前沿模型在最具经济价值领域的能力。该基准刻意不按 GDP 占比或 O\*NET 职业分类选取领域，而是覆盖芯片设计、网络安全、生物、金融、法律、量化交易、递归自我改进、硬件设计、材料科学、对齐和软件工程共 11 个方向，并与 14 家专业数据伙伴合作制作了 206 项任务。其最显著特点是难度：发布日得分最高的 Opus 5.5 仅得 12%，远低于其他基准常见的 50% 以上首日成绩。文章称，自 GDPx 上线以来，Anthropic、OpenAI、Google（Gemini 4 系列）、阿里巴巴和 Moonshot 均发布了新模型，但正文中的排行榜图片未提供可读的具体分数。

rss · Semianalysis · 11月26日 00:05

**「背景」** GDPx 由 SemiAnalysis 发布，包含 206 个任务、覆盖 11 个领域，每个任务都置于接近真实的工作环境中；据外部报道，其发布日期为 2026 年 11 月 2 日，首日得分最高的是 Claude Opus 5.5，为 12.0%，其后是 Gemini 4 Carbon 的 10.9% 和 GPT-6 Astra 的 9.6%。SemiAnalysis 在文中批评了按 GDP 占比或 O\*NET 职业分类选取领域的做法，并点名 OpenAI 于 2025 年 9 月推出的 GDPVal 以及 Agent&\#x27;s Last Exam；外部报道也称 GDPx 意在取代 GDPVal。

**「对评测的影响」** SemiAnalysis 指出，Fable 5.2 和 GPT-6.2 Astra 等模型因安全分类器在网络安全、生物和对齐三个领域触发拦截，整体得分被压低；若剔除这三个领域并对法律、金融改用部分评分，排名会发生变化。这意味着使用 GDPx 比较模型时，需注意安全策略和评分方式对结果的影响，不能直接按总分排序。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cellcog.ai/blog/gdpx-benchmark/">GDPx Benchmark : Claude Opus 5.5 Leads at Just 12% | CellCog</a></li>
<li><a href="https://sumus.im/blog/gdpx-benchmark">GDPx Benchmark : Scores, Leaderboard and What It Measures | Sumus</a></li>

</ul>
</details>

**标签**: `#benchmarking`, `#AI evaluation`, `#frontier models`, `#AI economics`

---

<a id="item-tech-news-10"></a>
### [三星与 SK 海力士据报交叉许可采用长江存储 Xtacking 技术](https://tech.ifeng.com/c/8yLRPKxQy4L) ⭐️ 7.0/10

据凤凰网报道，三星电子和 SK 海力士已通过交叉许可协议，同意在 3D NAND 闪存中采用长江存储 Xtacking 堆叠技术的部分内容。Xtacking 将存储单元阵列与控制电路（CMOS）分别制作在两片晶圆上，再通过键合工艺合二为一，使两部分可独立生产和优化。报道称三方均拒绝置评，协议的具体范围、许可条款和落地时间均未披露，因此这仍属未经企业确认的报道，而非已证实的量产安排。

telegram · zaihuapd · 11月25日 14:33

**「背景」** Xtacking 是长江存储自 2018 年推出的 3D NAND 架构，其核心是把存储单元阵列与外围 CMOS 逻辑电路分别制作在两片晶圆上，再通过等离子活化与热退火进行面对面键合。据 TrendForce 援引行业消息，长江存储在 2017 年至 2024 年 1 月间公开了 119 项混合键合相关专利，而三星截至 2023 年约有 83 项、SK 海力士仅 11 项。

**「影响」** 若报道属实，三星和 SK 海力士可在存储阵列与逻辑电路上分别选择工艺，Omdia 高级分析师指出厂商可自行生产存储阵列、把逻辑电路交给晶圆代工厂以使用更先进制程。但在企业确认前，相关工艺导入范围和量产影响仍不确定。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Yangtze_Memory_Technologies">Yangtze Memory Technologies - Wikipedia</a></li>
<li><a href="https://www.trendforce.com/news/2026/11/25/news-sk-hynix-reportedly-joins-samsung-in-licensing-ymtcs-xtacking-technology-as-nand-race-heats-up/">[News] SK hynix Reportedly Joins Samsung in Licensing ...</a></li>

</ul>
</details>

**标签**: `#3D NAND`, `#semiconductor manufacturing`, `#YMTC`, `#Samsung`, `#SK Hynix`

---

<a id="item-tech-news-11"></a>
### [1Password 确认安全事件：员工 GitHub 账户被入侵](https://9to5mac.com/2026/11/25/1password-confirms-security-incident-heres-what-you-need-to-know/) ⭐️ 7.0/10

1Password 确认发生安全事件：攻击者通过入侵一名员工的企业 GitHub 账户访问源代码，并向后台服务推送恶意代码，导致部分客户账户信息被下载，涉及姓名、邮箱地址、账户标识以及账户创建和最近登录时间。公司表示客户保险库及其中的内容未受影响，但未披露受影响用户数量。1Password 于 11 月 19 日开始调查该 GitHub 账户被入侵的迹象，目前已停用涉事账户、轮换或撤销可能暴露的内部凭证，并加强了邀请和恢复邮件的验证码。

telegram · zaihuapd · 11月26日 01:15

**「背景」** 1Password 官方博客称，公司于 2026 年 11 月 19 日开始调查员工企业 GitHub 账户被入侵的迹象，攻击者利用该账户访问源代码，并向后台服务推送恶意代码，后者下载了客户管理数据。此次事件的核心风险在于源代码与后台部署权限被滥用，而非保险库加密内容被直接攻破。

**「用户影响」** 1Password 表示用户无需更改账户，但应警惕利用泄露的姓名、邮箱和账户时间信息实施的钓鱼攻击。由于受影响用户数量未公布，用户无法判断自己是否在列，只能按公司提示对相关邮件保持谨慎。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://1password.com/blog/update-on-nov-2026-security-incident">Update on a security incident involving 1Password’s backend ...</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/1password-customer-data-stolen-after-employee-github-account-breach/">1Password customer data stolen after employee GitHub account ...</a></li>
<li><a href="https://thehackernews.com/2026/11/1password-hacked-customer-data-and.html">1Password Hacked, Customer Data and Source Code Stolen in ...</a></li>

</ul>
</details>

**标签**: `#security`, `#1password`, `#supply-chain`, `#github`, `#incident-response`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [美商务部被曝施压英特尔交出 10%股权](https://www.wired.com/story/inside-trumps-demands-to-another-chips-ceo/) ⭐️ 8.0/10

据 WIRED 报道，法庭文件显示，2025 年 8 月美国商务部律师在与英特尔首席财务官通话时警告，董事会可以拒绝交出 10%股权，但会面临“无法预测的后果”；几天后英特尔董事会交出股份，特朗普随后宣布美国政府未付钱即“完全拥有并控制”英特尔 10%股份，这批股份现值约 110 亿美元。

telegram · zaihuapd · 11月25日 13:25

**「背景」** 2025 年 8 月 22 日，英特尔宣布与特朗普政府达成协议，美国政府取得英特尔 10%的股份，商务部长卢特尼克确认了该持股安排。

**「影响」** 若报道属实，这一先例可能让接受美国政府补贴的芯片企业面临以股权换取支持的压力；据分析人士对媒体表示，政府选择哪些公司持股缺乏统一标准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.intel.com/content/www/us/en/newsroom/news/corporate/intel-and-trump-administration-reach-historic-agreement.html">Intel and Trump Administration Reach Historic Agreement to ...</a></li>
<li><a href="https://www.cnbc.com/2025/08/22/intel-goverment-equity-stake.html">U.S. takes 10% stake in Intel Trump expands control of ... - CNBC</a></li>
<li><a href="https://www.softwareseni.com/how-the-us-government-became-a-10-percent-intel-shareholder/">How the US Government Became Intel&#x27;s 10 Percent Shareholder ...</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#US government policy`, `#Intel`, `#corporate governance`, `#equity stake`

---

<a id="item-finance-news-2"></a>
### [美国拟对 14 个贸易伙伴加征第 301 条新关税](https://www.cnbc.com/2026/11/25/us-tariffs-trump-section-301.html) ⭐️ 8.0/10

美国政府拟依据 1974 年《贸易法》第 301 条，对中国、欧盟、日本、印度等 14 个贸易伙伴加征针对制造业结构性产能过剩的新关税，税率按国别设定，14 个伙伴已收到通知。对中国，新关税将在 2018 年已加征的 25%之上再加征 20%；若中国未遵守 2025 年 10 月在韩国釜山达成的贸易休战协议，对华新关税可能升至 40%。

telegram · zaihuapd · 11月25日 13:59

**「背景」** 美国贸易代表办公室已于 2026 年 3 月 11 日自行启动对这些经济体制造业“结构性产能过剩”的第 301 条调查，本次拟议关税是该调查的后续动作。中美两国领导人于 2025 年 10 月 30 日在韩国釜山会晤并达成为期一年的贸易休战，同意降低部分关税和出口管制。

**「影响」** 若落地，中国相关出口企业将面临在原有 25%基础上叠加 20%的税负，其他 13 个伙伴的出口商则按各自国别税率承担新增成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ustr.gov/about/policy-offices/press-office/press-releases/2026/november/ustr-makes-determinations-and-proposes-actions-14-section-301-investigations-relating-structural">USTR Makes Determinations and Proposes Actions in 14 Section ...</a></li>
<li><a href="https://www.hklaw.com/en/insights/publications/2026/11/ustr-proposes-tariffs-following-14-section-301">USTR Proposes Tariffs Following 14 Section 301 Manufacturing ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Busan_Summit">Busan Summit - Wikipedia</a></li>
<li><a href="https://www.cfr.org/articles/united-states-and-china-agree-trade-truce">United States and China Agree to Trade Truce | Council on ...</a></li>

</ul>
</details>

**标签**: `#US tariffs`, `#Section 301`, `#trade policy`, `#China-US trade`, `#manufacturing overcapacity`

---