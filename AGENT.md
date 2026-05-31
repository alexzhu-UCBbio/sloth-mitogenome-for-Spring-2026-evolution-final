# 课程期末项目协作指南

## 当前任务目标

在 `/Users/alexzhu/Desktop/Evolution_algorithm/Course_Final` 下共同完成分子演化课程期末大作业。项目基于 Delsuc et al. 2019 的树懒古线粒体基因组论文，核心是整理文献、复现主要系统发生分析，并写出结果比较、未来研究计划和 AI 使用声明。

主要文献：

- Delsuc, F. et al. Ancient Mitogenomes Reveal the Evolutionary History and Biogeography of Sloths. Current Biology 29, 2031-2042.e6 (2019).
- DOI: https://doi.org/10.1016/j.cub.2019.05.043
- 本地论文 PDF: `/Users/alexzhu/Documents/papers to read/More papers- for fun/演化课期末-树懒线粒体基因组.pdf`
- 本地复现计划 DOCX: `/Users/alexzhu/Desktop/Evolution_algorithm/Course_Final/Plan.docx`

默认用中文沟通和写作。报告正文必须用自己的中文表达，避免逐句翻译或照搬论文原句。

## 课程作业要求

最终作业需要覆盖以下内容：

1. 阅读并整理原文的研究问题、研究内容、主要方法和结论，写成约 1000 字的文章概要。
2. 复现其主要系统发生分析工作，包括下载序列、比对并进行系统发生树构建、贝叶斯定年分析等。复现过程使用的工具、参数、流程要详细描述。
3. 比较复现结果与文章报道结果，描述一致性和差异，并讨论可能原因。也可作为拓展修改部分分析参数和条件，比较结果变化。
4. 进一步思考文献中未解决的科学问题，结合分子演化课程内容设计未来研究计划，长度不超过 1000 字。
5. 文献引用规范，不得抄袭。
6. 若使用 AI 辅助，必须附 AI 使用声明，说明使用的 AI 工具、涉及部分、AI 生成结果中有哪些错误、自己如何检查并修改。使用 AI 不影响成绩，但使用而不声明会导致作业不合格。

## 已核对的工作区现状

当前目录下实际已有的核心文件和目录：

- `Plan.docx`: 之前拟定的复现计划。
- `input_dataset/Delsuc-CurrBiol-2019_dataset.fasta`: 作者整理好的线粒体基因组比对矩阵。本地检查到 40 条序列；论文方法报告最终 concatenated alignment 为 40 taxa、15,157 nt sites。
- `input_dataset/Delsuc-CurrBiol-2019_dataset.phylip`: 同一比对矩阵的 PHYLIP 格式版本。
- `model_partition/`
  - `Delsuc-CurrBiol-2019_dataset_partitions.nex`: 作者公开的 NEXUS 格式矩阵/分区文件，可作为分区模型分析输入。
  - `Delsuc-CurrBiol-2019_TableS1_PartitionFinder_RAxML_best_partition_scheme.txt`
  - `Delsuc-CurrBiol-2019_TableS2_ModelFinder_IQ-TREE_best_partition_scheme.txt`
  - `Delsuc-CurrBiol-2019_TableS3_PartitionFinder_MrBayes_best_partition_scheme.txt`
- `published_trees/`
  - `Delsuc-CurrBiol-2019_FigS2_RAxML_MLtree_100BP_nexus_for_FigTree.tree`
  - `Delsuc-CurrBiol-2019_FigS3_IQ-TREE_MLtree_100BP_nexus_for_FigTree.tree`
  - `Delsuc-CurrBiol-2019_FigS4_MrBayes_consensus_nexus_for_FigTree.tree`
  - `Delsuc-CurrBiol-2019_FigS5_PhyloBayes_consensus_nexus_for_FigTree.tree`
  - `Delsuc-CurrBiol-2019_FigS6_PhyloBayes_chronogram_nexus_for_FigTree.tree`

当前重要缺口：

- Zenodo 主输入文件已经基本齐全；下一步不需要先补下载 `.nex` 或 `.phylip`。
- 默认 shell 中 `seqkit` 尚不可用。后续若要运行 QC，需要先配置 conda/mamba 环境，或用 Python/Biopython 替代。
- 仍需确认当前 IQ-TREE 版本能否直接识别 `model_partition/Delsuc-CurrBiol-2019_dataset_partitions.nex`；该 `.nex` 同时包含矩阵和分区信息，实际命令可能与只传独立 partition file 的写法不同。

不要直接沿用旧计划中假定的 `data_raw/zenodo/` 或 `data/raw/` 状态。那些是建议目录，不是当前已经存在的事实。若新建目录，优先保留现有 `input_dataset/`、`model_partition/`、`published_trees/`，再增加 `metadata/`、`results/`、`scripts/`、`report/`。

## 原文关键事实

研究对象和问题：

- 现生树懒只剩 Bradypus 和 Choloepus 两个属，但第四纪之前树懒有丰富的地栖和岛屿类群。
- 传统系统发生主要依赖形态性状，通常把 Bradypus 作为其他树懒的姐妹群，并把 Choloepus 与加勒比树懒或 Megalonyx 相关类群放在 Megalonychidae 中。
- 论文用古 DNA 线粒体基因组检验这些形态分类框架，重建树懒系统发育和生物地理历史。

数据：

- 新测序 10 个灭绝树懒 mitogenomes，覆盖 Mylodon、Megatherium、Megalonyx、Nothrotheriops、Parocnus、Acratocnus 等主要晚第四纪类群。
- GenBank 新增 accession: `MK903494`-`MK903503`。
- 原始 Illumina reads: ENA `PRJEB32380`。
- 作者公开的 capture baits、alignment、trees 在 Zenodo: https://doi.org/10.5281/zenodo.2658746
- 系统发生矩阵包含 25 个现生 xenarthran、1 个 extinct glyptodont、已有 extinct Mylodon、新增 10 个 extinct sloth mitogenomes、3 个 afrotherian outgroups，共 40 taxa。
- 所有线粒体基因纳入分析，但不包括 control region。
- 24 个 tRNA 和 2 个 rRNA 以 nucleotide level 用 MAFFT G-INSI 比对；13 个蛋白编码基因用 translation-aware alignment；Gblocks relaxed settings 去除不可靠区域。
- 最终矩阵为 15,157 个可明确比对的核苷酸位点。

原文系统发生方法：

- 初始 42 个分区：13 个 protein-coding genes 的 3 个 codon positions 共 39 个分区，加 12S rRNA、16S rRNA、所有 tRNAs。
- PartitionFinder v2.1.1 和 ModelFinder 用 greedy algorithm，BIC 选择模型/分区方案，分区搜索时 branch lengths unlinked。
- RAxML v8.1.22: best-fitting partitioned model，branches linked across final partitions，100 nonparametric bootstrap pseudo-replicates。
- IQ-TREE 方法部分写 v1.6.6；本地 TableS2 日志显示 IQ-TREE 1.6.3 built Mar 22 2018，random seed `991127`，40 taxa、14 partitions、15,157 sites，100 bootstrap。报告中要区分“论文方法写法”和“本地补充表日志信息”。
- MrBayes v3.2.6: 两个独立 runs，每个 4 条 heated MCMCMC chains，10,000,000 generations，每 1000 generations sample，前 2500 trees burn-in；ASDSF < 0.05、ESS > 100、PSRF 1.00-1.02；15,000 combined post-burn-in trees 生成 50% majority-rule consensus。
- PhyloBayes MPI v1.7b: CAT-GTR+G4，两个独立 chains，18,000 cycles，每 cycle sampling，前 1800 trees burn-in；bpcomp / tracecomp 检查 ASDSF < 0.05、ESS > 1000；32,400 post-burn-in trees 生成 consensus。

原文贝叶斯定年方法：

- 原文定年使用 PhyloBayes v4.1c，不是 BEAST。
- 模型为 CAT-GTR+G4，relaxed molecular clock，birth-death prior on divergence times，soft fossil calibrations。
- 拓扑固定为 RAxML、IQ-TREE、MrBayes under best partition model 得到的树。
- fossil calibration intervals:
  - Paenungulata: max 71.2 Ma, min 55.6 Ma
  - Xenarthra: max 71.2 Ma, min 58.5 Ma
  - Pilosa: max 65.5 Ma, min 31.5 Ma
  - Vermilingua: max 61.1 Ma, min 15.97 Ma
  - Tolypeutinae: max 37.8 Ma, min 23.0 Ma
- Folivora ancestral node left unconstrained。
- Placentalia root prior set to 100 Ma。
- clock model cross-validation 比较 LN、UGAM、strict clock。learning set 13,642 sites，test set 1,515 sites，10 random replicates，每个 learning-set MCMC 1100 cycles，前 100 samples burn-in。LN 最优。
- final dating: autocorrelated lognormal relaxed clock，两个独立 chains，50,000 cycles，每 10 cycles sample，前 500 samples burn-in，用 `tracecomp` 检查 ESS，用 `readdiv` 汇总 divergence dates。

## 原文主要结论锚点

这些是比较复现结果时的目标参照，不要为了“匹配”而改结果：

- 加勒比树懒单系，支持率强。
- 加勒比树懒不是现生二趾树懒 Choloepus 的近亲；它们可能是其他树懒的姐妹群，但这个深层位置支持率较弱。
- Choloepus 与 Mylodon 聚为一支，支持率强。
- Bradypus 不是所有其他树懒的姐妹群，而是嵌入包括 Megatherium、Megalonyx、Nothrotheriops 的地栖树懒相关分支。
- 分子树识别 8 个主要树懒 lineage/family，分为 3 个主要 clades。
- 8 个 family 大约在 36-28 Ma 之间起源。
- 加勒比树懒早期分化约 35 +/- 5 Ma，和 GAARlandia 假说提出的 35-33 Ma 陆桥时间相容。
- Acratocnus 与 Parocnus 约 29 +/- 5 Ma 分化；Choloepus 与 Mylodon 约 29 +/- 5 Ma 分化；Bradypus 与 Megalonyx + Nothrotheriops 约 29 +/- 5 Ma 分化；Megalonyx 与 Nothrotheriops 约 28 +/- 5 Ma 分化。

## 复现边界

主线应基于作者公开的 curated mitogenomic dataset，而不是从 raw FASTQ 重新做古 DNA 组装。

必须做或优先做：

- 审计本地 alignment：taxon 数、序列长度、缺失/ambiguous/gap 情况、taxon names。
- 可选下载或核对 GenBank `MK903494`-`MK903503`，用于数据来源追溯；若课程要求中的“下载序列”已接受作者 Zenodo alignment，则这一步不是建树主输入。
- 核对现有 Zenodo alignment、PHYLIP 和 NEXUS 分区文件是否能被分析软件读取。
- 用作者 alignment 和 partition 信息复跑 IQ-TREE 最大似然树。
- 将复现树与 `published_trees/Delsuc-CurrBiol-2019_FigS3_IQ-TREE_MLtree_100BP_nexus_for_FigTree.tree` 比较。
- 整理 `published_trees/Delsuc-CurrBiol-2019_FigS6_PhyloBayes_chronogram_nexus_for_FigTree.tree` 的主要定年结果。
- 写作时清楚区分“原文报告”“本项目复现”“拓展分析”。

可选拓展：

- IQ-TREE 1000 ultrafast bootstrap + SH-aLRT，与 100 standard bootstrap 比较支持率变化。
- RAxML / MrBayes / PhyloBayes 拓扑复现。
- PhyloBayes dating 严格复现。
- BEAST2 简化定年只能作为拓展近似，不能称为原文严格复现，因为原文定年不是 BEAST。

不建议作为主线：

- 从 ENA raw FASTQ 重新 trimming、mapping、assembly、consensus calling。
- 复现捕获探针设计。
- 复现全部古 DNA wet-lab 流程。
- 复现完整牙齿性状祖先状态重建，除非时间充足且用户明确要求。

## 建议目录

保留当前已有目录，并在需要时增加：

- `metadata/`: taxon list、GenBank accession summary、clade annotation。
- `results/qc/`: alignment 和 GenBank QC。
- `results/iqtree/`: IQ-TREE 输出。
- `results/tree_comparison/`: topology notes、RF distance、clade comparison。
- `results/dating/`: chronogram node age notes。
- `results/figures/`: 树图和定年图。
- `scripts/`: 可复现脚本。
- `report/`: 最终中文报告分段。

建议最终交付物：

- `metadata/taxa_from_dataset.tsv`
- `results/qc/alignment_summary.tsv`
- `metadata/genbank_sequence_summary.tsv`
- `results/iqtree/delsuc2019_iqtree_standard_bootstrap.treefile`
- `results/iqtree/delsuc2019_iqtree_standard_bootstrap.iqtree`
- `results/tree_comparison/topology_comparison_notes.md`
- `results/dating/key_node_age_notes.md`
- `results/figures/reproduced_iqtree_tree.pdf`
- `results/figures/published_chronogram_annotated.pdf`
- `report/01_article_summary.md`
- `report/02_methods_reproduction.md`
- `report/03_result_comparison.md`
- `report/04_future_plan.md`
- `report/05_ai_statement.md`

## 推荐执行顺序

1. 数据盘点和环境记录：列出现有 Zenodo FASTA、PHYLIP、NEXUS、模型表和发表树文件，记录来源和日期。
2. Alignment QC：检查 `input_dataset/Delsuc-CurrBiol-2019_dataset.fasta` 是否 40 taxa、15,157 sites、所有序列等长，并输出 QC 表。
3. GenBank 下载核对：下载 `MK903494`-`MK903503` 的 FASTA 和 GenBank 格式，整理长度、描述、N 比例、对应 taxon。
4. IQ-TREE 复现：优先用作者 alignment + partition file + 100 standard bootstrap；记录版本、命令、seed、runtime、log-likelihood、best-fit model/partition。
5. 树比较：比较 taxa、关键 clades、bootstrap 支持率；可选计算 RF distance。
6. 定年整理：读取 FigS6 PhyloBayes chronogram，标注主要节点年龄；若 PhyloBayes / BEAST2 拓展不可行，要解释原因。
7. 写作整合：文章概要、复现流程、结果比较、未来计划、AI 使用声明、参考文献。

## IQ-TREE 复现命令模板

在确认当前 IQ-TREE 版本后，优先尝试：

```bash
mkdir -p results/iqtree

iqtree2 \
  -s input_dataset/Delsuc-CurrBiol-2019_dataset.fasta \
  -p model_partition/Delsuc-CurrBiol-2019_dataset_partitions.nex \
  -m MFP+MERGE \
  -b 100 \
  -T AUTO \
  --seed 991127 \
  --prefix results/iqtree/delsuc2019_iqtree_standard_bootstrap
```

如果当前 IQ-TREE 版本不接受 `-p` 或 `--seed`，按版本帮助调整参数，但必须在报告中记录实际命令和版本。

可选拓展版：

```bash
iqtree2 \
  -s input_dataset/Delsuc-CurrBiol-2019_dataset.fasta \
  -p model_partition/Delsuc-CurrBiol-2019_dataset_partitions.nex \
  -m MFP+MERGE \
  -B 1000 \
  -alrt 1000 \
  -T AUTO \
  --prefix results/iqtree/delsuc2019_iqtree_ufboot1000
```

若最终只能跑 unpartitioned 或重新推断分区，要明确写成“近似/拓展”，不能写成严格复现原文 partitioned analysis。

## 比较复现结果时要检查

Taxon 层面：

- published tree 和 reproduced tree 是否包含相同 taxa。
- taxon label 是否因旧名称、下划线、空格、引号不一致导致比较失败。
- 注意本地 TableS2 日志中的部分旧名如 `Megatheriidae_undet_LibX18`、`Megatherium_sp_LibEmil`，而 published tree / FASTA 可能使用 `Megatherium_americanum_...` 等更新名。

关键拓扑层面：

- `Choloepus` 是否与 `Mylodon` 成组。
- `Bradypus` 是否嵌入 `Megatherium + Megalonyx + Nothrotheriops` 相关分支。
- `Acratocnus + Parocnus` 加勒比树懒是否单系。
- 加勒比树懒相对其他树懒的深层位置支持率是否较低。
- `Megalonyx + Nothrotheriops`、`Megatherium`、`Bradypus` 的相对关系是否和原文 FigS3 大体一致。

整体树层面：

- 可用 R `ape` / `phangorn` 计算 RF distance，但报告中不要只报 RF 值，要解释生物学关键节点是否一致。
- rooting 方式会影响视觉判断；原文树文件用于 FigTree 展示时可能有 root 标记，但 IQ-TREE 输出本质是 unrooted ML tree。比较时以 clade split 为主。

## 写作要求

文章概要：

- 约 1000 中文字，覆盖研究背景、核心问题、数据来源、主要方法、主要结论。
- 不要逐句翻译 abstract 或 summary。
- 建议突出“灭绝类群改变了对现生树懒关系和形态趋同的理解”。

复现方法：

- 写清楚每个输入文件来源、下载日期、软件版本、命令、参数、seed、输出文件。
- 将“使用作者整理好的 alignment 复现系统树”和“从 GenBank 下载 10 个新增 mitogenome 进行来源核对”分开说明。
- 如果没有从 raw reads 重组装，要坦诚说明边界和原因。

结果比较：

- 分成最大似然树比较、支持率比较、定年结果比较、差异来源讨论。
- 可能差异来源包括：IQ-TREE 版本、bootstrap 类型、随机种子、ModelFinder 重新选择模型、partition merge 差异、taxon label 差异、MCMC 收敛、古 DNA 缺失位点和线粒体仅代表母系历史。

未来研究计划：

- 不超过 1000 字。
- 可选方向：核基因组/核基因位点验证物种树；增加古 DNA 时空采样；整合形态和分子 total-evidence tip-dating；用 BioGeoBEARS 检验 GAARlandia 和加勒比扩散模型；比较线粒体树和核基因组树的冲突。

AI 使用声明：

- 必须包含 Codex/OpenAI 等工具名称。
- 说明 AI 辅助了哪些部分：文献要点整理、流程抽取、命令草拟、结果比较框架、中文润色等。
- 说明 AI 可能或实际出现的错误：如混淆 BEAST 与 PhyloBayes、假设本地已有 partition file、软件版本不一致、路径与真实工作区不一致等。
- 说明用户如何检查和修改：对照原文 PDF、Plan.docx、Zenodo 文件、命令日志、树文件和软件输出。

## 协作注意事项

- 在运行耗时分析前，先确认输入文件和参数，不要盲目启动长 MCMC。
- 网络下载需要记录 URL、日期和 checksum 或文件大小。
- 不要把 BEAST2 结果写成原文严格复现；如果做，只能作为参数/框架变化的拓展比较。
- 不要再假设当前工作区缺少 partition NEXUS；实际文件在 `model_partition/Delsuc-CurrBiol-2019_dataset_partitions.nex`。
- 报告中引用文献时使用规范格式，至少引用原文、IQ-TREE、RAxML、MrBayes、PhyloBayes、MAFFT、Gblocks、PartitionFinder/ModelFinder 等实际用到的软件或方法文献。
- 如果有不确定事实，优先回到 PDF、Plan.docx、Zenodo 文件和实际运行日志核对。
