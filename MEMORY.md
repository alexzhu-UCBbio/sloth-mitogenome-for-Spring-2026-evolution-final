# Project Memory

更新日期：2026-05-31

## 项目目标

在 `/Users/alexzhu/Desktop/Evolution_algorithm/Course_Final` 中完成分子演化课程期末项目。项目基于 Delsuc et al. 2019 关于古树懒线粒体基因组的论文，重点是整理文献、复现主要系统发生分析、比较复现结果与原文、提出未来研究计划，并附 AI 使用声明。

主要文献：

- Delsuc, F. et al. Ancient Mitogenomes Reveal the Evolutionary History and Biogeography of Sloths. Current Biology 29, 2031-2042.e6 (2019).
- DOI: https://doi.org/10.1016/j.cub.2019.05.043
- 本地 PDF：`/Users/alexzhu/Documents/papers to read/More papers- for fun/演化课期末-树懒线粒体基因组.pdf`
- 本地计划：`Plan.docx`

## 当前重要结论

- 主分析复现应使用作者 Zenodo 公开的 curated mitogenomic alignment，而不是从 raw reads 重新组装。
- `input_dataset/Delsuc-CurrBiol-2019_dataset.fasta` 可以视为本项目系统发生分析主输入之一；它已经是作者整理、比对、筛选后的矩阵。
- GenBank `MK903494`-`MK903503` 是原文新增 10 个灭绝树懒线粒体基因组的数据库 accession。下载它们可用于数据来源核对，但不是建树主线的必要输入。
- 原文贝叶斯定年使用 PhyloBayes，不是 BEAST。若之后做 BEAST2，只能写作拓展近似，不能写作严格复现。
- 用户不希望在每次回答末尾反复出现“当前目录不是 git 仓库/无法给出 git diff”这类无关说明。现在本目录已经是 git 仓库。

## 已有核心文件

输入矩阵：

- `input_dataset/Delsuc-CurrBiol-2019_dataset.fasta`
- `input_dataset/Delsuc-CurrBiol-2019_dataset.phylip`

分区/模型相关：

- `model_partition/Delsuc-CurrBiol-2019_dataset_partitions.nex`
- `model_partition/Delsuc-CurrBiol-2019_TableS1_PartitionFinder_RAxML_best_partition_scheme.txt`
- `model_partition/Delsuc-CurrBiol-2019_TableS2_ModelFinder_IQ-TREE_best_partition_scheme.txt`
- `model_partition/Delsuc-CurrBiol-2019_TableS3_PartitionFinder_MrBayes_best_partition_scheme.txt`

发表树：

- `published_trees/Delsuc-CurrBiol-2019_FigS2_RAxML_MLtree_100BP_nexus_for_FigTree.tree`
- `published_trees/Delsuc-CurrBiol-2019_FigS3_IQ-TREE_MLtree_100BP_nexus_for_FigTree.tree`
- `published_trees/Delsuc-CurrBiol-2019_FigS4_MrBayes_consensus_nexus_for_FigTree.tree`
- `published_trees/Delsuc-CurrBiol-2019_FigS5_PhyloBayes_consensus_nexus_for_FigTree.tree`
- `published_trees/Delsuc-CurrBiol-2019_FigS6_PhyloBayes_chronogram_nexus_for_FigTree.tree`

## 已完成工作

1. 重写并更新了 `AGENT.md`，将旧的、误导性的工作区状态修正为当前真实状态。
2. 确认 `dataset.fasta` 包含 40 条序列 / 40 个 taxon labels / 15,157 个比对位点。
3. 确认 `dataset.phylip` 文件头为 `40 15157`，与 FASTA 是同一套矩阵的 PHYLIP 格式。
4. 确认 `dataset_partitions.nex` 是 NEXUS 格式文件，包含 `ntax = 40`、`nchar = 15157` 的矩阵，并在 `begin paup;` 中给出 37 个 gene-level `charset` 坐标。
5. 创建并修改了 `scripts/00_dataset_qc.py`。现在该脚本只生成两个 TSV：
   - `results/qc/alignment_summary.tsv`
   - `results/qc/dataset_qc_summary.tsv`
6. 运行了数据 QC，结果显示 FASTA、PHYLIP、NEXUS 三者 taxon labels 一致。
7. 将本地项目初始化为 git 仓库，并连接到 GitHub remote：
   - `https://github.com/alexzhu-UCBbio/sloth-mitogenome-for-Spring-2026-evolution-final.git`

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

`results/qc/alignment_summary.tsv` 的列：

```text
taxon
length
gap_count
N_count
missing_count
ambiguous_count
other_count
gap_fraction
N_fraction
missing_fraction
ambiguous_fraction
other_fraction
```

总体 QC 解释：

- 全矩阵共 `40 x 15157 = 606,280` 个字符。
- gap、N、`?` 和 ambiguous base 比例都很低。
- 未检测到其他非法字符。
- 该 alignment 可以继续用于最大似然系统发生树构建。

## 当前环境状态

- Python 可用：`python3` 来自 miniconda base。
- R 可用：`/opt/homebrew/bin/R`。
- `mamba` 和 `conda` 可用。
- `iqtree` / `iqtree2` 当前不可用，需要安装或激活相应环境。

建议安装命令：

```bash
mamba create -n sloth_phylo -c conda-forge -c bioconda iqtree seqkit biopython r-base r-ape r-phangorn -y
conda activate sloth_phylo
```

## 下一步建议

1. 安装或激活 IQ-TREE 环境，并记录软件版本。
2. 根据 `dataset_partitions.nex` 中的 gene coordinates 生成 IQ-TREE 可用的原始 42-partition 文件：
   - 13 个 protein-coding genes x 3 个 codon positions = 39
   - 12S rRNA = 1
   - 16S rRNA = 1
   - all tRNAs 合并 = 1
3. 用 `MFP+MERGE` 跑 IQ-TREE 分区模型和 100 次 standard bootstrap，尽量贴近原文。
4. 与原文 FigS3 IQ-TREE 发表树比较：
   - taxa 是否一致
   - `Choloepus + Mylodon` 是否复现
   - `Bradypus` 是否嵌入地栖树懒相关分支
   - `Acratocnus + Parocnus` 加勒比树懒是否单系
   - bootstrap 支持率是否接近
5. 整理 FigS6 PhyloBayes chronogram 的关键节点时间，作为贝叶斯定年结果对照。
6. GenBank `MK903494`-`MK903503` 下载可以之后作为来源核对和报告补充，不是当前建树主线阻塞项。

## 写作提醒

- 报告中应明确区分“原文方法”“本项目复现”“可选拓展”。
- 不要把 BEAST2 写成原文定年复现。
- 不要把只用 FASTA 的非分区树写成严格复现；正式复现应使用分区模型。
- AI 使用声明必须写明使用 Codex/OpenAI 辅助了文献整理、流程设计、脚本草拟、结果解释和文字润色；也要写明用户如何用论文、Zenodo 文件、脚本输出和树文件核对。
