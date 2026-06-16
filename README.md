# 树懒古线粒体基因组系统发生复现项目

本仓库用于分子演化课程期末项目，围绕 Delsuc et al. (2019) 关于树懒古线粒体基因组的研究，整理作者公开数据并复现主要系统发生分析。项目主线基于作者在 Zenodo 公开的 curated mitogenomic alignment，而不是从原始测序 reads 重新组装古 DNA。

主要论文：

- Delsuc, F. et al. Ancient Mitogenomes Reveal the Evolutionary History and Biogeography of Sloths. Current Biology 29, 2031-2042.e6 (2019).
- DOI: https://doi.org/10.1016/j.cub.2019.05.043
- Zenodo 数据：https://doi.org/10.5281/zenodo.2658746

## 目录说明

### `input_dataset/`

存放系统发生分析的输入矩阵和定年分析辅助输入。

主要文件包括：

- `Delsuc-CurrBiol-2019_dataset.fasta`：作者整理好的线粒体基因组比对矩阵，40 个 taxon、15,157 个位点。
- `Delsuc-CurrBiol-2019_dataset.phylip`：同一矩阵的 PHYLIP 格式，是多数建树软件的主输入。
- `Delsuc-CurrBiol-2019_dataset.PML`：用于 PAML / MCMCTree 的矩阵格式。
- `delsuc2019_calibrations.txt`：定年分析中整理的化石校准信息。
- `delsuc2019_fixed_topology_iqtree_clean_rooted.tre`：用于定年拓展分析的固定拓扑树。

### `model_partition/`

存放分区模型和作者补充表中的模型选择结果。

主要文件包括：

- `Delsuc-CurrBiol-2019_dataset_partitions.nex`：作者公开的 NEXUS 矩阵和 gene-level 分区信息。
- `Delsuc-CurrBiol-2019_iqtree_42partitions.partitions`：按原文初始方案生成的 42 个 IQ-TREE 分区。
- `raxml_4partitions.partitions`：从作者 RAxML 分区方案整理出的 4 个分区。
- `Delsuc-CurrBiol-2019_TableS*_...txt`：作者补充表中的 PartitionFinder / ModelFinder 最优分区和模型结果。

### `published_trees/`

存放论文公开发表的对照树文件，用于比较复现结果。

包括 RAxML、IQ-TREE、MrBayes、PhyloBayes consensus tree，以及 PhyloBayes chronogram。比较复现结果时主要参考这些文件，而不是只看论文正文图。

### `scripts/`

存放本项目中用于数据检查和分区整理的脚本。

主要文件包括：

- `00_dataset_qc.py`：检查 FASTA / PHYLIP / NEXUS 数据集的 taxon 数、序列长度、标签一致性等。
- `01_make_iqtree_42_partitions.py`：从 NEXUS 分区坐标生成 IQ-TREE 可读的 42-partition 文件。

### `logs/`

存放关键分析运行日志，便于追踪实际命令、软件输出和运行状态。

主要包括：

- RAxML 最大似然树、bootstrap 和支持率标注日志。
- MrBayes 10,000,000 generations 运行日志。
- PhyloBayes 拓扑复现的服务器试跑/运行日志。

### `results/`

存放本项目的主要复现结果。这里保留的是可复查的关键输出，小型树文件、摘要表、日志和图。

主要子目录：

- `results/qc/`：数据集 QC 输出，例如 alignment summary 和 42 分区覆盖情况。
- `results/iqtree/`：IQ-TREE 复现结果，包括 `.treefile`、`.contree`、`.iqtree`、`.log` 和最优分区方案。
- `results/raxml/`：RAxML 复现结果，包括 best tree、bootstrap trees、带支持率的 bipartition tree 和运行信息。
- `results/mrbayes/`：MrBayes 复现结果。posterior sample 原始链未纳入仓库。
- `results/phylobayes/`：PhyloBayes CAT-GTR+G4 拓扑复现的汇总结果。关键文件是 `bpcomp.con.tre`、原始 `.chain`、`.trace`、`.treelist` 文件未纳入仓库。
- `results/MDGUI_dating/`：PhyloSuite / PAML MCMCTree 拓展定年结果。
- `results/visualization/`：已生成的树图 PDF，用于报告写作和结果检查。

## 复现范围说明

本项目已经复现或整理了以下内容：

- 作者 curated alignment 的数据 QC。
- IQ-TREE 最大似然树复现。
- RAxML 最大似然树和 100 次 bootstrap 复现。
- MrBayes 分区贝叶斯系统树复现。
- PhyloBayes CAT-GTR+G4 拓扑复现。
- PhyloBayes 定年，这里我们使用PAML MCMCTree复现。

需要注意的是，原文严格的贝叶斯定年使用 PhyloBayes v4.1c。仓库中的 `results/MDGUI_dating/` 是 PAML MCMCTree 替代复现。

## 文件管理说明

为避免仓库过大，以下类型文件不提交到 GitHub：

- PhyloBayes 原始 MCMC 链：`.chain`、`.trace`、`.treelist` 等。
- MCMCTree 每个 run 的大体积链文件和完整运行目录。
- IQ-TREE / MrBayes 的 checkpoint、posterior sample 和其他中间文件。

GitHub 仓库中保留的是关键的的输入数据、脚本、关键树文件、日志、摘要结果和图件。
