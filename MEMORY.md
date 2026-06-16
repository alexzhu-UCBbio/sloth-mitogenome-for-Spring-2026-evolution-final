# Project Memory

更新日期：2026-06-15

## 项目目标

在 `/Users/alexzhu/Desktop/Evolution_algorithm/Course_Final` 中完成分子演化课程期末项目。项目基于 Delsuc et al. 2019 关于古树懒线粒体基因组的论文，重点是整理文献、复现主要系统发生分析、比较复现结果与原文、提出未来研究计划，并附 AI 使用声明。

主要文献：

- Delsuc, F. et al. Ancient Mitogenomes Reveal the Evolutionary History and Biogeography of Sloths. Current Biology 29, 2031-2042.e6 (2019).
- DOI: https://doi.org/10.1016/j.cub.2019.05.043
- 本地 PDF：`/Users/alexzhu/Documents/papers to read/More papers- for fun/演化课期末-树懒线粒体基因组.pdf`
- `Plan.docx` 已从当前仓库删除，不再作为当前核心文件依赖。

## 当前重要结论

- 截至 2026-06-15，项目分析阶段已完成；后续工作转入结果核对、图表整理和中文报告写作。
- 主分析复现使用作者 Zenodo 公开的 curated mitogenomic alignment，而不是从 raw reads 重新组装。
- `input_dataset/Delsuc-CurrBiol-2019_dataset.fasta` / `.phylip` 是本项目系统发生分析主输入；矩阵为 40 taxa、15,157 sites。
- 原文 IQ-TREE 复现主线应严格区分：
  - 原文方法写 IQ-TREE v1.6.6。
  - 作者 TableS2 日志显示 IQ-TREE 1.6.3 built Mar 22 2018，seed `991127`，最终 14 partitions，100 standard bootstrap。
  - 本项目实际复现使用 IQ-TREE 3.1.2 for MacOS ARM 64-bit built May 17 2026。
- 原文贝叶斯定年使用 PhyloBayes，不是 BEAST。若之后做 BEAST2，只能写作拓展近似，不能写作严格复现。
- GenBank `MK903494`-`MK903503` 是原文新增 10 个灭绝树懒线粒体基因组的 accession；下载核对可作为数据来源补充，但不是当前 ML 建树主输入。
- MrBayes 原文长度运行已经完成；当前可用于报告的是拓扑和 posterior probability 支持率。参数层面仍有部分 branch-length / rate-multiplier 相关指标 ESS 偏低，写作时不能夸大为所有参数完全收敛。
- MrBayes 产生 4 个 consensus tree 是因为 TableS3/MrBayes block 使用 `unlink brlens=(all)`，即同一拓扑下每个分区单独估计一套枝长。四棵树不是四套互相冲突的系统发育结论。
- FigS5 / S5 的 PhyloBayes MPI CAT-GTR+G4 拓扑复现链、`bpcomp` / `tracecomp` 诊断和发表 FigS5 对比已经完成。拓扑 posterior convergence 达标，consensus tree 与发表 FigS5 的 40 taxa 和全部非平凡 splits 一致；tracecomp 中少数连续参数 ESS 未达到原文 `>1000` 标准，写作时需如实说明。
- 本机 Apple Silicon + `osx-64` / Rosetta 环境可以运行 PhyloBayes，但实测太慢：`-np 8` 本机试跑约 3.5 天/单链，不适合完整两链复现。正式 S5 复现使用服务器。
- 服务器为 `user-Rack-Server`，`x86_64`，Intel Xeon Platinum 8462Y+，2 sockets x 32 cores/socket x 2 threads/core = 64 physical cores / 128 logical CPUs。服务器实测 S5 PhyloBayes 速度约 2.7-3.5 秒/cycle，单链约 14-18 小时。
- `results/MDGUI_dating/` 已重新替换并核对为可用的树懒项目 PhyloSuite / MCMCTree 输出：输入为 `Delsuc-CurrBiol-2019_dataset.PML`，40 taxa、15,157 sites；calibration tree 含五个 fossil `B(...)` calibration 和 root `<1.0000`。8 个 runs 的 `mu`、`sigma2`、`lnL` 已回到一致量级；repeat1/repeat2 汇总结果高度一致。该结果可作为快速替代/拓展定年分析使用。
- FigS6 / S6 的原文严格 PhyloBayes dating 仍未完成。原文 S6 定年使用 PhyloBayes v4.1c，而不是 PhyloBayes MPI v1.7b/1.9；当前 MCMCTree 结果不能写成原文严格 FigS6 复现，只能写成 PAML MCMCTree 拓展/近似分析。

## 已有核心文件

输入矩阵：

- `input_dataset/Delsuc-CurrBiol-2019_dataset.fasta`
- `input_dataset/Delsuc-CurrBiol-2019_dataset.phylip`

分区/模型相关：

- `model_partition/Delsuc-CurrBiol-2019_dataset_partitions.nex`
- `model_partition/Delsuc-CurrBiol-2019_iqtree_42partitions.partitions`
- `model_partition/raxml_4partitions.partitions`
- `model_partition/Delsuc-CurrBiol-2019_TableS1_PartitionFinder_RAxML_best_partition_scheme.txt`
- `model_partition/Delsuc-CurrBiol-2019_TableS2_ModelFinder_IQ-TREE_best_partition_scheme.txt`
- `model_partition/Delsuc-CurrBiol-2019_TableS3_PartitionFinder_MrBayes_best_partition_scheme.txt`

发表树：

- `published_trees/Delsuc-CurrBiol-2019_FigS2_RAxML_MLtree_100BP_nexus_for_FigTree.tree`
- `published_trees/Delsuc-CurrBiol-2019_FigS3_IQ-TREE_MLtree_100BP_nexus_for_FigTree.tree`
- `published_trees/Delsuc-CurrBiol-2019_FigS4_MrBayes_consensus_nexus_for_FigTree.tree`
- `published_trees/Delsuc-CurrBiol-2019_FigS5_PhyloBayes_consensus_nexus_for_FigTree.tree`
- `published_trees/Delsuc-CurrBiol-2019_FigS6_PhyloBayes_chronogram_nexus_for_FigTree.tree`

IQ-TREE 复现输出：

- `results/iqtree/iqtree_standard.iqtree`
- `results/iqtree/iqtree_standard.treefile`
- `results/iqtree/iqtree_standard.contree`
- `results/iqtree/iqtree_standard.best_scheme`
- `results/iqtree/iqtree_standard.best_scheme.nex`
- `results/iqtree/iqtree_standard.log`

RAxML 复现输出：

- `results/raxml/RAxML_bestTree.raxml_ml`
- `results/raxml/RAxML_bootstrap.raxml_bs`
- `results/raxml/RAxML_bipartitions.raxml_standard`
- `results/raxml/RAxML_bipartitionsBranchLabels.raxml_standard`
- `results/raxml/RAxML_info.raxml_ml`
- `results/raxml/RAxML_info.raxml_bs`
- `results/raxml/RAxML_info.raxml_standard`
- `logs/raxml_ml.log`
- `logs/raxml_bs.log`
- `logs/raxml_standard.log`

MrBayes 复现输出：

- `results/mrbayes/mrbayes_10m.nex`
- `results/mrbayes/mrbayes_10m.nex.run1.p`
- `results/mrbayes/mrbayes_10m.nex.run2.p`
- `results/mrbayes/mrbayes_10m.nex.pstat`
- `results/mrbayes/mrbayes_10m.nex.lstat`
- `results/mrbayes/mrbayes_10m.nex.mcmc`
- `results/mrbayes/mrbayes_10m.nex.tree1.con.tre`
- `results/mrbayes/mrbayes_10m.nex.tree2.con.tre`
- `results/mrbayes/mrbayes_10m.nex.tree3.con.tre`
- `results/mrbayes/mrbayes_10m.nex.tree4.con.tre`
- `results/mrbayes/mrbayes_10m.nex.tree1.tstat`
- `results/mrbayes/mrbayes_10m.nex.tree1.parts`
- `logs/mrbayes_10m.log`

PhyloBayes S5 拓扑复现输出：

- 本机 conda 环境：`/opt/homebrew/Caskroom/miniconda/base/envs/phylobayes`
- 本机试跑命令使用 `mpirun -np 8 pb_mpi -d input_dataset/Delsuc-CurrBiol-2019_dataset.phylip -cat -gtr -dgam 4 -x 1 18000 results/phylobayes/consensus_run1`
- 当前本地输出目录：`results/phylobayes/`
- run1 输出前缀：`results/phylobayes/consensus_run1`
- run2 输出前缀：`results/phylobayes/consensus_run2`
- 本机试跑日志：`logs/phylobayes_consensus_run1.log`
- 当前文件：`consensus_run1/2.trace`、`.treelist`、`.param`、`.chain`、`.monitor`、`.run`
- run1 trace：18,001 行，treelist：18,000 行。
- run2 trace：18,001 行，treelist：18,000 行。
- 模型用途：S5 topology 复现，CAT-GTR+G4；不是 S6 relaxed-clock dating。
- `bpcomp` / `tracecomp` 输出已经拷回本地：
  - `results/phylobayes/phylobayes_bpcomp.log`
  - `results/phylobayes/phylobayes_tracecomp.log`
  - `results/phylobayes/bpcomp.bplist`
  - `results/phylobayes/bpcomp.con.tre`
- `bpcomp` 使用 burn-in 1,800，每条链保留 16,200 trees，合计 32,400 post-burn-in trees；`maxdiff = 0.0344444`，低于原文 `0.05` 标准。
- `tracecomp` 使用 burn-in 1,800，每条链 sample size 为 16,200；多数连续参数 ESS > 1000，但 `loglik = 886`、`statalpha = 714` 低于原文 `>1000` 标准。
- `bpcomp.con.tre` 与发表 FigS5 的 40 taxa 和全部非平凡 splits 一致，关键树懒节点 posterior probability 基本一致；树懒深层主干处的 polytomy 应解释为短枝和后验拓扑不确定性的 consensus 表现。
- 服务器主机：`user-Rack-Server`；CPU：Intel Xeon Platinum 8462Y+，64 physical cores / 128 logical CPUs。
- 服务器 log 已确认模型和数据正确：CAT-GTR+G4、40 taxa、15,157 sites、4 nucleotide states、chain name `results/consensus_run1`、`run started`。
- 服务器 log 中 OpenMPI 的 CMA / `openib` / `librdmacm.so.1` warning 为性能/组件提示，不是致命错误；如果后续重启可用 `--mca btl ^openib --mca btl_vader_single_copy_mechanism none` 降低噪音。

PhyloBayes FigS6 / S6 dating 待准备路径：

- 本地发表 chronogram 对照：`published_trees/Delsuc-CurrBiol-2019_FigS6_PhyloBayes_chronogram_nexus_for_FigTree.tree`
- 本地 fixed topology 候选：
  - `results/iqtree/iqtree_standard.treefile`
  - `results/raxml/RAxML_bipartitions.raxml_standard`
  - `results/mrbayes/mrbayes_10m.nex.tree*.con.tre`
  - 服务器 S5 完成后也可把 PhyloBayes consensus tree 作为补充拓扑对照，但原文 dating 描述固定到 RAxML、IQ-TREE、MrBayes best partition model trees。
- S6 输出目录建议：`results/phylobayes_dating/`
- S6 日志目录建议：`logs/phylobayes_dating_*.log`
- S6 前置检查：服务器或本机是否有 PhyloBayes v4.1c / dating 版命令、`readdiv`、`tracecomp`，以及 fossil calibration / fixed-topology 输入格式。

PhyloSuite / MCMCTree 目录检查：

- 已检查目录：`results/MDGUI_dating/`
- 目录大小约 `1.4G`。
- 顶层文件包括：`FigTree.tre`、`PhyloSuite_MCMCTREE.log`、`summary and citation.txt`。
- 子目录包括：`repeat1/run1` 到 `repeat1/run4`，以及 `repeat2/run5` 到 `repeat2/run8`。
- 输入矩阵：`Delsuc-CurrBiol-2019_dataset.PML`，文件头为 `40  15157`，taxon 包括 `Acratocnus_ye_Lib58`、`Bradypus_*`、`Dasypus_*`、`Dugong_dugon_NC_003314`、`Loxodonta_africana_NC_000934`、`Orycteropus_afer_NC_002078` 等本项目 taxon。
- calibration tree：`repeat1/calibration_tree.nwk` 和 `repeat2/calibration_tree.nwk` 均含 `B(0.1597,0.6110,0.025,0.025)`、`B(0.3150,0.6550,0.025,0.025)`、`B(0.2300,0.3780,0.025,0.025)`、`B(0.5850,0.7120,0.025,0.025)`、`B(0.5560,0.7120,0.025,0.025)` 和 root `<1.0000`。
- MCMCTree 版本/辅助工具：`summary and citation.txt` 记录为 MCMCTREE v4.10.9，PhyloSuite v2，ETE3；当前替换后结果运行时间为 2026-06-15 18:23:52 到 19:28:09，总用时约 1:04:16。
- `mcmctree.ctl` 关键参数：`seqtype = 0`，`usedata = 2 out.BV`，`clock = 3`，`model = 7`，`alpha = 0.5`，`ncatG = 4`，`cleandata = 0`，`burnin = 250000`，`sampfreq = 100`，`nsample = 50000`。
- 每个 run 的 `mcmc.txt` 为 50,002 行；每个 repeat 的 `all_mcmc_runs.txt` 为 200,005 行，对应每个 repeat 汇总 4 个 runs。
- `repeat1/summarization.out.txt` 和 `repeat2/summarization.out.txt` 均已生成 posterior mean / 95% CI / 95% HPD 表；顶层和 repeat 目录均有 `FigTree.tre`。用户已替换原先异常的定年结果；当前结果已核对，repeat1/repeat2 关键节点年龄几乎一致。
- MCMCTree `FigTree.tre` 与发表 FigS6 chronogram 的 40 taxa 和全部无根 split 一致，RF distance = 0。关键树懒深层节点年龄趋势相近，但 MCMCTree 多数略老：Folivora 约 36.84 Ma vs 发表 FigS6 35.47 Ma；Caribbean sloths 31.54 Ma vs 29.20 Ma；`Choloepus + Mylodon` 31.11 Ma vs 29.16 Ma；`Bradypus + Megalonyx + Nothrotheriops` 32.04 Ma vs 29.36 Ma；`Megalonyx + Nothrotheriops` 29.75 Ma vs 28.43 Ma。
- 该结果可用于本项目“快速 MCMCTree 拓展定年”部分，但不能写成原文 PhyloBayes FigS6 的严格复现。

可视化输出当前为未追踪文件：

- `results/visualization/Delsuc-CurrBiol-2019_FigS3_IQ-TREE_MLtree_100BP_nexus_for_FigTree.tree.pdf`
- `results/visualization/iqtree_standard.treefile.pdf`

## 已完成工作

1. 重写并更新了 `AGENT.md`，将旧的、误导性的工作区状态修正为当前真实状态。
2. 确认 `dataset.fasta` 包含 40 条序列 / 40 个 taxon labels / 15,157 个比对位点。
3. 确认 `dataset.phylip` 文件头为 `40 15157`，与 FASTA 是同一套矩阵的 PHYLIP 格式。
4. 确认 `dataset_partitions.nex` 是 NEXUS 格式文件，包含 `ntax = 40`、`nchar = 15157` 的矩阵，并在 `begin paup;` 中给出 37 个 gene-level `charset` 坐标。
5. 创建并运行 `scripts/00_dataset_qc.py`，生成：
   - `results/qc/alignment_summary.tsv`
   - `results/qc/dataset_qc_summary.tsv`
6. 运行数据 QC，结果显示 FASTA、PHYLIP、NEXUS 三者 taxon labels 一致。
7. 创建 `scripts/01_make_iqtree_42_partitions.py`，从 `dataset_partitions.nex` 读取 gene coordinates，并按原文初始分区方案生成 42 partitions：
   - 12S rRNA = 1
   - 16S rRNA = 1
   - 13 个 protein-coding genes x 3 个 codon positions = 39
   - all tRNAs 合并 = 1
8. 运行 IQ-TREE 复现，命令为：

```bash
iqtree \
  -s input_dataset/Delsuc-CurrBiol-2019_dataset.phylip \
  -p model_partition/Delsuc-CurrBiol-2019_iqtree_42partitions.partitions \
  -m MFP \
  --merge greedy \
  --merit BIC \
  -b 100 \
  -T 8 \
  --seed 991127 \
  --prefix results/iqtree/iqtree_standard
```

9. 本地项目已初始化为 git 仓库，并连接到 GitHub remote：
   - `https://github.com/alexzhu-UCBbio/sloth-mitogenome-for-Spring-2026-evolution-final.git`
10. 已有提交记录包括：
   - `Run IQ-TREE standard bootstrap`
   - `Ignore IQ-TREE intermediate files`
11. 从作者 TableS1 抽取并验证 RAxML 4 分区文件 `model_partition/raxml_4partitions.partitions`：
   - Subset1 = 7,875 sites
   - Subset2 = 3,554 sites
   - Subset3 = 3,554 sites
   - Subset4 = 174 sites
   - 总覆盖 15,157 sites，missing sites = 0，重复位点 = 0。
12. 使用 RAxML 8.2.9 完成分子矩阵 RAxML 复现三步法：
   - 原始 alignment 上搜索 best ML tree。
   - 100 次 standard nonparametric bootstrap。
   - 将 bootstrap 支持率标注到 best ML tree 上。
13. 确认 `sloth_phylo` 环境中 MrBayes 可用：
   - `mrbayes 3.2.7`
   - `mb`
   - `mb-mpi`
   - `openmpi 4.1.6`
14. 按 TableS3 的 4-subset MrBayes partition scheme 准备并运行原文长度 MrBayes 分析：
   - 2 independent runs。
   - 每个 run 4 条 heated MCMCMC chains。
   - 10,000,000 generations。
   - 每 1000 generations sample。
   - `burnin=2500`。
   - `unlink brlens=(all)`，因此输出 4 套分区枝长 consensus trees。
15. MrBayes 完整运行已经结束：
   - 最终 generation：`10,000,000`。
   - 最终 ASDSF：`0.000884`。
   - wall time：`3 hours 36 mins 30 seconds`。
   - `sump` / `sumt` 使用两个 runs，每个 run 10001 samples，其中 7501 samples included，总计 15002 samples。
16. 初步比较 MrBayes posterior probability：
   - `Choloepus + Mylodon`：PP = 1.000000。
   - Caribbean sloths (`Acratocnus + Parocnus`)：PP = 1.000000。
   - `Megalonyx + Nothrotheriops`：PP 约 0.999933。
   - `Bradypus + Megalonyx + Nothrotheriops`：PP = 1.000000。
   - `Megatherium + Bradypus + Megalonyx + Nothrotheriops`：PP = 1.000000。
   - 非加勒比树懒大枝：PP 约 0.724，说明深层位置支持相对弱。
17. 比较四套 MrBayes 分区枝长与发表 FigS4：
   - `tree1`、`tree2`、`tree3`、`tree4` 的 topology/splits 与发表 FigS4 一致。
   - `tree3.con.tre` 与发表 FigS4 枝长最接近：MAE `0.05047`，RMSE `0.08556`，本地总枝长 `5.51367`，发表 FigS4 总枝长 `9.31419`。
   - `tree3` 对应 TableS3 Subset3，即多数 protein-coding genes 的 third codon positions。
18. 检查并安装 PhyloBayes MPI 环境：
   - 本机 `base` / `sloth_phylo` 中原本无 `pb_mpi`、`bpcomp`、`tracecomp`、`readdiv`。
   - PhyloSuite 插件目录中没有可用 PhyloBayes；现有插件包括 IQ-TREE、MrBayes、RAxML/PartitionFinder、MAFFT、Gblocks、PAML、ASTRAL 等。
   - 本机已创建 conda 环境 `phylobayes`，路径为 `/opt/homebrew/Caskroom/miniconda/base/envs/phylobayes`。
19. 本机完成 PhyloBayes CAT-GTR+G4 试跑与测速：
   - 命令模型为 `-cat -gtr -dgam 4`，对齐原文 CAT-GTR+G4。
   - 输入为 `input_dataset/Delsuc-CurrBiol-2019_dataset.phylip`，log 显示 40 taxa、15,157 sites、4 states。
   - 本机 `-np 8` 速度约 3.5 天/单链；两链完整复现预计约 7 天，不适合作为正式 S5 复现平台。
20. 已完成 PhyloBayes S5 两条链、收敛诊断和 FigS5 对比：
   - 服务器为 Linux x86_64，Intel Xeon Platinum 8462Y+ 双路 64 物理核 / 128 逻辑线程。
   - 本地目录为 `results/phylobayes/`。
   - run1 和 run2 均有 `.chain`、`.monitor`、`.param`、`.run`、`.trace`、`.treelist`。
   - 两条链的 `.trace` 均为 18,001 行，`.treelist` 均为 18,000 行，对应原文 S5 的 18,000 cycles。
   - `bpcomp` 丢弃前 1,800 trees 后每条链保留 16,200 trees，合计 32,400 post-burn-in trees；`maxdiff = 0.0344444`。
   - `tracecomp` 中多数连续参数 ESS > 1000；`loglik = 886`、`statalpha = 714` 未达到原文 `>1000` 标准。
   - `bpcomp.con.tre` 与发表 FigS5 在 40 taxa 和全部非平凡 splits 上一致；关键树懒节点 PP 基本一致。
21. 已重新替换并核对 `results/MDGUI_dating/`：
   - 目录结构为 PhyloSuite / MCMCTree 输出，包括 `repeat1`、`repeat2` 和 8 个 run 子目录。
   - 输入已经是本项目树懒矩阵：`Delsuc-CurrBiol-2019_dataset.PML`，40 taxa、15,157 sites。
   - calibration tree 包含五个 fossil soft-bound `B(...)` calibration 和 root `<1.0000`。
   - 用户已替换此前异常的结果；两个 repeat 均完成 summarization，可用于 MCMCTree 拓展定年结果整理和与发表 FigS6 的趋势比较。
   - 8 个 runs 的 `mu` 约 0.335、`sigma2` 约 0.241-0.243、`lnL` 约 -39.16 到 -39.23，未再出现原先 run6 的异常量级。
   - repeat1/repeat2 的关键节点年龄几乎一致；MCMCTree 拓扑与发表 FigS6 的 40 taxa 和全部无根 split 一致。
   - 该结果仍不是原文 PhyloBayes v4.1c 的严格 FigS6 复现。
22. 分析阶段已完成；下一步是自由核对现有输出、与发表树/chronogram 比较，并进入报告写作。
   - 不能把 S5 的 `pb_mpi` 拓扑命令或 MCMCTree 结果写成 S6 PhyloBayes dating 严格复现。
   - 定年部分应写成：整理发表 FigS6 chronogram 作为原文对照，同时将 `results/MDGUI_dating/` 作为 PAML MCMCTree 拓展/近似定年结果比较。

## QC 结果

`results/qc/dataset_qc_summary.tsv` 当前结果：

```text
fasta_sequence_count        40
fasta_unique_taxon_labels   40
fasta_length_values         {15157: 40}
phylip_header_ntax          40
phylip_header_nchar         15157
phylip_unique_taxon_labels  40
nexus_unique_taxon_labels   40
fasta_vs_phylip_same_taxa   True
fasta_vs_nexus_same_taxa    True
```

总体 QC 解释：

- 全矩阵共 `40 x 15157 = 606,280` 个字符。
- gap、N、`?` 和 ambiguous base 比例都很低。
- 未检测到其他非法字符。
- 该 alignment 可以继续用于最大似然系统发生树构建。

## IQ-TREE 复现结果

本项目 IQ-TREE 运行记录：

- 软件：IQ-TREE 3.1.2 for MacOS ARM 64-bit built May 17 2026。
- 硬件/线程：MacBook Air，`-T 8`。
- seed：`991127`。
- 输入：40 taxa，15,157 total sites。
- 初始输入分区：42 partitions。
- IQ-TREE 3.1.2 + `MFP --merge greedy --merit BIC` 后，`.iqtree` 记录为 32 partitions。
- 最佳模型/分区记录见 `results/iqtree/iqtree_standard.iqtree`。
- partition model：edge-linked-proportional partition model with separate substitution models and separate rates across sites。
- log-likelihood：`-185607.0262`。
- CPU time：`30327.38792 seconds (8h:25m:27s)`。
- wall-clock time：`12594.82372 seconds (3h:29m:54s)`。
- 完成时间：`Mon Jun 1 04:04:44 2026`。

原文 TableS2 对照：

- 作者 TableS2 日志为 IQ-TREE 1.6.3。
- 原文/TableS2 输入为 40 taxa、15,157 sites。
- 作者最终为 14 partitions。
- 作者 TableS2 log-likelihood：`-185829.8416`。
- 作者 TableS2 CPU time：`25566.3 seconds (7h:6m:6s)`。
- 作者 TableS2 wall-clock time：`4106.3 seconds (1h:8m:26s)`。

解释时要强调：本项目严格按原文主线使用作者 curated alignment、42 初始分区、ModelFinder、BIC、greedy merge、100 standard bootstrap 和 seed `991127`；但软件版本不同，最终合并分区数、模型选择和似然值不要求完全一致，这正是可讨论差异。

## RAxML 复现结果

本项目 RAxML 运行记录：

- 软件：RAxML 8.2.9 from PhyloSuite/PartitionFinder plugin，executable 为 `/Users/alexzhu/Desktop/Evolution_algorithm/ASTAR_workspace/PhyloSuite/plugins/partitionfinder-2.1.1/programs/raxml_pthreads`。
- 原文软件：RAxML v8.1.22。
- 硬件/线程：MacBook Air，`-T 8`。
- 输入：`input_dataset/Delsuc-CurrBiol-2019_dataset.phylip`，40 taxa，15,157 sites。
- 分区：作者 TableS1 的 PartitionFinder RAxML best scheme，4 subsets，文件为 `model_partition/raxml_4partitions.partitions`。
- 模型：TableS1 每个 subset 为 `GTR+I+G`，RAxML 命令使用 `-m GTRGAMMAI`。
- 枝长设置：命令未使用 `-M`；RAxML log 显示 `Using 4 distinct models/data partitions with joint branch length optimization`，对应原文 `linking branches across the best-fitting partitions`。
- seed：`-p 991127`，bootstrap 使用 `-b 991127`。注意原文没有公开 RAxML seed；`991127` 来自作者 IQ-TREE TableS2 日志，只能作为本项目可复现 seed。
- 第一步 ML search log-likelihood：`-190098.096915`。
- 第一步 ML search 用时：`62.393264 seconds`。
- 第二步 100 bootstrap 总用时：`2001.046514 seconds`，平均每个 bootstrap `20.010465 seconds`。
- 第三步 bipartition 标注用时：`0.014086 seconds`。
- 最终用于比较和画图的 RAxML 树：`results/raxml/RAxML_bipartitions.raxml_standard`。

与原文方法对齐情况：

- 已对齐：作者 curated alignment、TableS1 4-subset 分区、`GTR+I+G` 对应的 `GTRGAMMAI`、linked branch lengths、100 standard nonparametric bootstrap。
- 未完全对齐/未知：RAxML 版本不同；原文未公开 RAxML 完整命令、seed、是否多次独立 ML search、额外优化参数。
- 本地扫读论文 PDF 后，正文和补充表没有发现更多可用于校准 RAxML 枝长的公开细节。

RAxML 枝长发现：

- 复现 RAxML 最终树总枝长约 `17.399894`。
- 发表 FigS2 RAxML 树总枝长约 `10.906727`。
- 复现 RAxML 枝长整体约为发表 FigS2 的 `1.60x`，明显偏长。
- 作为诊断，曾尝试 `GTRGAMMA` 的 ML-only 运行，枝长没有改善，反而更长，因此不建议用 `GTRGAMMA` 替代 TableS1 对应的 `GTRGAMMAI`。
- 不建议继续为匹配发表枝长而手动调模型或缩放枝长。RAxML 复现应主要用于拓扑和 bootstrap 支持率比较；枝长一致性更适合参考 IQ-TREE 复现，因为 IQ-TREE 复现树总枝长约 `10.268435`，发表 FigS3 约 `10.037442`。

## 树比较观察

整体结构：

- 3 个 Afrotheria 外群（`Orycteropus_afer`、`Dugong_dugon`、`Loxodonta_africana`）与 Xenarthra 内群分开。
- Xenarthra 内部分为 Cingulata 和 Pilosa 两个主要大枝。
- Cingulata 包括 `Dasypus`、`Euphractus`、`Chaetophractus`、`Zaedyus`、`Cabassous`、`Tolypeutes`、`Priodontes`、`Calyptophractus`、`Chlamyphorus`、`Doedicurus` 等犰狳及 glyptodont 相关类群。
- Pilosa 包括 Vermilingua（`Cyclopes`、`Myrmecophaga`、`Tamandua` 等食蚁兽）和 Folivora（树懒）。

树懒关键结论：

- `Choloepus` 是现生二趾树懒，`Bradypus` 是现生三趾树懒。
- `Mylodon` 是已灭绝地栖树懒；`Mylodon_darwinii` 可称为达尔文磨齿兽/达尔文地懒。
- `Choloepus` 与 `Mylodon` 聚为一支，支持率高，是复现原文关键结论之一。
- `Bradypus` 不与 `Choloepus` 直接互为姐妹群，而是与 `Megalonyx`、`Nothrotheriops` 等灭绝地栖树懒相关分支更接近。
- 加勒比树懒为 `Acratocnus_ye_Lib58` 和 `Parocnus_serus_Lib54`。它们在树懒类外侧形成一对，但其深层位置支持较弱。

支持率观察：

- 一个树懒深层节点在复现中 bootstrap 为 `49`，发表 FigS3 中相应节点约为 `41`。这说明树懒主要谱系之间的深层分叉顺序不稳定，不能作为强支持结论。
- `53` 支持率节点位于 Cingulata 内部，涉及 `Cabassous`、`Tolypeutes`、`Priodontes`、`Calyptophractus`、`Chlamyphorus` 等犰狳类群之间的关系。
- 强支持节点和弱支持节点应分开讨论：`Choloepus + Mylodon`、`Bradypus` 内部、`Megatherium` 内部等较稳定；深层短枝附近更不稳定。

枝长观察：

- IQ-TREE 枝长表示 substitutions per site，不是时间。
- 复现树与发表 FigS3 在主要内部枝长上总体接近，无明显系统性偏离。
- RAxML 复现树的枝长尺度与发表 FigS2 不一致，整体约长 `1.60x`。该差异不应通过结果导向的模型调整或手动缩放来消除，应作为版本/未公开命令细节导致的复现差异保留。
- 根部附近的枝长差异不应过度解释，因为 IQ-TREE 输出本质是无根树，FigTree reroot 会把外群与 Xenarthra 之间的一条无根枝切分为两段。根部两侧枝长比例可能是显示/root placement 结果，不是稳定生物学差异。

Mylodon 局部拓扑：

- 发表 FigS3 中：`Mylodon_darwinii_Lib67` 与 `Mylodon_darwinii_NC_037941` 先聚在一起，再与 `Mylodon_listai_Lib16` 聚合。
- 复现树中：`Mylodon_darwinii_Lib67` 与 `Mylodon_listai_Lib16` 先聚在一起，再与 `Mylodon_darwinii_NC_037941` 聚合。
- 该局部差异支持率很低（发表约 40，复现为 43），且相关枝长极短，不应解读为强支持的物种关系改变。

## 可视化状态

- 本地有 `/Applications/FigTree v1.4.4.app`，但 macOS app launcher 识别 Java 有问题。
- 系统 Java 可用：OpenJDK 25.0.2。
- 可绕过 app launcher，直接用 jar 打开：

```bash
java -jar "/Users/alexzhu/Desktop/Evolution_algorithm/ASTAR_workspace/FigTree/lib/figtree.jar" \
  results/iqtree/iqtree_standard.treefile
```

- 打开 IQ-TREE `.treefile` 时，FigTree 会询问节点/分支标签名称，可保留为 `label`。复现树 bootstrap 在 FigTree 中用 `Node Labels -> Display: label` 显示。
- 作者 FigS3 NEXUS 树自带 FigTree 配置，bootstrap 属性名为 `BP`，用 `Node Labels -> Display: BP` 显示。
- FigTree 字体设置：
  - 物种名：`Tip Labels -> Font`。
  - bootstrap 数字：`Node Labels -> Font`。
  - 导出建议用 `File -> Export PDF`，不要用截图作为最终图。

## 当前 git 状态提醒

截至 2026-06-12，本地有以下未追踪文件：

```text
-
input_dataset/Delsuc-CurrBiol-2019_dataset.phylip.reduced
logs/
model_partition/raxml_4partitions.partitions
results/iqtree/iqtree_standard.best_model.nex
results/iqtree/iqtree_standard.bionj
results/iqtree/iqtree_standard.boottrees
results/iqtree/iqtree_standard.ckp.gz
results/iqtree/iqtree_standard.mldist
results/iqtree/iqtree_standard.model.gz
results/qc/partition_42_summary.tsv
results/raxml/
results/visualization/
```

不要盲目 `git add .`。IQ-TREE 中间文件如 `.ckp.gz`、`.bionj`、`.mldist`、`.model.gz` 通常不提交。RAxML 关键输出可考虑提交 `RAxML_bestTree.raxml_ml`、`RAxML_bootstrap.raxml_bs`、`RAxML_bipartitions.raxml_standard`、`RAxML_info.*` 和 `logs/raxml_*.log`；RAxML 自动生成的 `.reduced` 文件是否保留需要用户确认。`boottrees` 和可视化 PDF 是否提交需要用户确认。根目录有一个名为 `-` 的未追踪小文件，需要确认来源后再处理。

## 后续计划状态

旧的“安装 IQ-TREE、生成 42 分区、运行 IQ-TREE、运行 RAxML、运行 MrBayes”主线已经完成。

后续计划：

1. 分析阶段已完成。IQ-TREE、RAxML、MrBayes、PhyloBayes S5 拓扑复现和 MCMCTree 拓展定年均已有可用输出；后续不再启动新的长时间系统发育/MCMC 分析，除非用户明确要求。
2. 结果核对阶段：新替换的 `results/MDGUI_dating/` repeat/run 收敛、关键节点年龄映射，以及与发表 FigS6 chronogram 的趋势差异已完成初步核对；后续只需在写作前按报告需要复查具体数字。
3. 写作阶段：整合 IQ-TREE、RAxML、MrBayes、PhyloBayes S5 和 MCMCTree 拓展定年结果，清楚区分“原文方法”“本项目复现”“拓展/近似分析”。
4. 图表阶段：保留 FigS3/FigS5 拓扑对比、FigS6 chronogram 对照和 MCMCTree 关键节点年龄表。若补充 RF distance 或 clade table，只作为支持材料，不作为阻塞项。
5. GenBank accession 核对仍为可选补充。若时间不足，可只说明作者 Zenodo curated alignment 是主输入，`MK903494`-`MK903503` 作为原文新增灭绝树懒 mitogenome accession 记录。

## 写作提醒

- 报告中应明确区分“原文方法”“本项目复现”“可选拓展”。
- 不要把 BEAST2 写成原文定年复现。
- 不要把只用 FASTA 的非分区树写成严格复现；正式复现应使用分区模型。
- IQ-TREE 复现部分要写明版本差异：原文方法 v1.6.6、作者 TableS2 v1.6.3、本项目 v3.1.2。
- MrBayes 复现部分要写明版本差异：原文 v3.2.6、本项目 v3.2.7；posterior probability 支持关键拓扑，但部分枝长/速率相关参数 ESS 偏低。
- 定年部分要区分发表 FigS6 chronogram 整理和本项目是否真的重跑 PhyloBayes dating。
- 结果比较中要强调关键拓扑基本一致，同时讨论支持率、分区合并数、log-likelihood、Mylodon 局部拓扑和 root/枝长显示差异。
- AI 使用声明必须写明使用 Codex/OpenAI 辅助了文献整理、流程设计、脚本草拟、结果解释和文字润色；也要写明用户如何用论文、Zenodo 文件、脚本输出、IQ-TREE 日志和树文件核对。
