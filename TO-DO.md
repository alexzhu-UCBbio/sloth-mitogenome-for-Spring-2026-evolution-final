# TO-DO: 定年与 PhyloBayes 收尾

更新日期：2026-06-15

## 当前状态

IQ-TREE、RAxML、MrBayes 的主要系统发生树复现已经完成。

FigS5 / S5 的 PhyloBayes MPI CAT-GTR+G4 拓扑复现链已经完成并拷回本地 `results/phylobayes/`。当前已有两条 independent chains，各 18,000 trees / 18,001 行 trace。它已经有初步结果可分析，但还差 `bpcomp` / `tracecomp` 收敛诊断，以及与发表 FigS5 的关键拓扑和 posterior probability 比较。

`results/MDGUI_dating/` 已重新检查，现在是树懒项目的 PhyloSuite / MCMCTree 输出。输入为 `Delsuc-CurrBiol-2019_dataset.PML`，40 taxa、15,157 sites；calibration tree 含五个 fossil `B(...)` calibration 和 root `<1.0000`。该结果可作为快速替代/拓展定年分析使用。

FigS6 / S6 的原文严格 PhyloBayes relaxed-clock chronogram 仍未完成。原文 S6 是分子定年分析，不是拓扑树重建；不能用 S5 的 `pb_mpi -cat -gtr -dgam 4` 命令直接替代。

项目边界保持不变：

- 主输入仍是作者公开 curated mitogenomic alignment，不从 raw reads 重新组装。
- 原文定年使用 PhyloBayes v4.1c，不是 BEAST。
- BEAST2 或 PAML MCMCtree 只能作为拓展近似，不能写成原文 FigS6 严格复现。
- 如果最终没有重跑 PhyloBayes dating，只能写成“整理发表 FigS6 chronogram”，不能写成“复现了贝叶斯定年”。
- 当前 `results/MDGUI_dating/` 可以用于 MCMCTree 拓展定年，但写作时必须明确它不是原文 PhyloBayes 严格复现。

## FigS5 / S5 当前结果

本地结果目录：

- `results/phylobayes/`
- 目录大小约 `2.8G`。
- run1 前缀：`results/phylobayes/consensus_run1`
- run2 前缀：`results/phylobayes/consensus_run2`

已有文件：

- `consensus_run1.chain`
- `consensus_run1.monitor`
- `consensus_run1.param`
- `consensus_run1.run`
- `consensus_run1.trace`
- `consensus_run1.treelist`
- `consensus_run2.chain`
- `consensus_run2.monitor`
- `consensus_run2.param`
- `consensus_run2.run`
- `consensus_run2.trace`
- `consensus_run2.treelist`

检查结果：

- run1 trace：18,001 行；treelist：18,000 行。
- run2 trace：18,001 行；treelist：18,000 行。
- trace header 为 `iter time topo loglik length alpha Nmode statent statalpha rrent rrmean`。
- 该结果对应 S5 拓扑复现的 CAT-GTR+G4 MCMC chains，不是 S6 dating。
- 目录中尚未看到 `bpcomp` / `tracecomp` 输出。

S5 收尾命令：

```bash
bpcomp \
  -x 1800 1 \
  -o results/phylobayes/delsuc2019_catgtrg4_bpcomp \
  results/phylobayes/consensus_run1 \
  results/phylobayes/consensus_run2 \
  > logs/phylobayes_bpcomp.log 2>&1
```

```bash
tracecomp \
  -x 1800 1 \
  results/phylobayes/consensus_run1 \
  results/phylobayes/consensus_run2 \
  > logs/phylobayes_tracecomp.log 2>&1
```

S5 还要记录：

- 两条 chains 是否都达到 18,000 cycles。
- burn-in 是否按 1,800 samples。
- ASDSF 是否 < 0.05。
- ESS 是否 > 1000。
- post-burn-in combined trees 是否为 32,400。
- consensus tree 与发表 FigS5 的关键拓扑和 PP 是否一致。

## MDGUI / MCMCTree 当前目录

已检查目录：

- `results/MDGUI_dating/`
- 目录大小约 `1.4G`。
- 顶层有 `FigTree.tre`、`PhyloSuite_MCMCTREE.log`、`summary and citation.txt`。
- 有 `repeat1/run1` 到 `repeat1/run4`，以及 `repeat2/run5` 到 `repeat2/run8`。
- 每个 run 有 `mcmctree.ctl`、`mcmc.txt`、`mcmc.out.txt`、`mcmc_for_sum.txt`、`FigTree.tre`、`calibration_tree.nwk`、`Delsuc-CurrBiol-2019_dataset.PML`、`out.BV`、`rst*`、`tmp0001.*` 等。

检查结果：

- `Delsuc-CurrBiol-2019_dataset.PML` 文件头是 `40  15157`。
- taxon 为本项目树懒/贫齿类/外群 taxon，包括 `Acratocnus_ye_Lib58`、`Bradypus_*`、`Dasypus_*`、`Dugong_dugon_NC_003314`、`Loxodonta_africana_NC_000934`、`Orycteropus_afer_NC_002078` 等。
- calibration tree 包含：
  - `B(0.1597,0.6110,0.025,0.025)`
  - `B(0.3150,0.6550,0.025,0.025)`
  - `B(0.2300,0.3780,0.025,0.025)`
  - `B(0.5850,0.7120,0.025,0.025)`
  - `B(0.5560,0.7120,0.025,0.025)`
  - root `<1.0000`
- `summary and citation.txt` 记录 MCMCTREE v4.10.9，PhyloSuite v2，ETE3；运行时间约 1:01:37。
- `mcmctree.ctl` 关键参数为 `usedata = 2 out.BV`、`clock = 3`、`model = 7`、`ncatG = 4`、`cleandata = 0`、`burnin = 250000`、`sampfreq = 100`、`nsample = 50000`。
- 每个 run 的 `mcmc.txt` 为 50,002 行；每个 repeat 的 `all_mcmc_runs.txt` 为 200,005 行。
- `repeat1/summarization.out.txt` 和 `repeat2/summarization.out.txt` 均已生成 posterior mean / 95% CI / 95% HPD 表。
- 该结果可用于 MCMCTree 拓展定年；不能写成原文 PhyloBayes FigS6 严格复现。

## FigS6 原文方法

原文 FigS6 / chronogram 的关键方法：

- Software：PhyloBayes v4.1c。
- Substitution model：CAT-GTR+G4。
- Clock model：relaxed molecular clock。
- Final clock：autocorrelated lognormal relaxed clock。
- Divergence-time prior：birth-death prior on divergence times。
- Fossil calibrations：soft fossil calibration intervals。
- Topology：固定为 RAxML、IQ-TREE、MrBayes under best partition model 得到的树。
- Folivora ancestral node：unconstrained。
- Placentalia root prior：100 Ma。
- Final dating：2 independent chains，50,000 cycles，每 10 cycles sample。
- Burn-in：first 500 samples。
- Diagnostics：`tracecomp` 检查 ESS。
- Summary：`readdiv` 汇总 divergence dates。

Clock model cross-validation：

- 比较 LN、UGAM、strict clock。
- Learning set：13,642 sites。
- Test set：1,515 sites。
- 10 random replicates。
- 每个 learning-set MCMC：1,100 cycles。
- Burn-in：first 100 samples。
- 原文结果：LN 最优。

Fossil calibration intervals：

- Paenungulata：maximum 71.2 Ma，minimum 55.6 Ma。
- Xenarthra：maximum 71.2 Ma，minimum 58.5 Ma。
- Pilosa：maximum 65.5 Ma，minimum 31.5 Ma。
- Vermilingua：maximum 61.1 Ma，minimum 15.97 Ma。
- Tolypeutinae：maximum 37.8 Ma，minimum 23.0 Ma。

## FigS6 输入和路径

本地发表 chronogram 对照：

- `published_trees/Delsuc-CurrBiol-2019_FigS6_PhyloBayes_chronogram_nexus_for_FigTree.tree`

主 alignment：

- `input_dataset/Delsuc-CurrBiol-2019_dataset.phylip`
- `input_dataset/Delsuc-CurrBiol-2019_dataset.fasta`

固定拓扑候选：

- IQ-TREE：`results/iqtree/iqtree_standard.treefile`
- RAxML：`results/raxml/RAxML_bipartitions.raxml_standard`
- MrBayes：`results/mrbayes/mrbayes_10m.nex.tree1.con.tre` 到 `tree4.con.tre`

建议新增目录：

- `results/phylobayes_dating/`
- `logs/phylobayes_dating_*.log`
- `results/dating/`

建议输出文件：

- `results/dating/key_node_age_notes.md`
- `results/phylobayes_dating/README.md`
- 若严格 dating 成功，再保存 `tracecomp`、`readdiv`、calibration、fixed topology 和 chain 输出。

## 下一步清单

1. 对 `results/phylobayes/consensus_run1` 和 `results/phylobayes/consensus_run2` 运行 `bpcomp -x 1800 1`，记录 ASDSF、maxdiff、生成的 consensus tree。
2. 对同两条链运行 `tracecomp -x 1800 1`，记录各参数 ESS，判断是否达到原文报告标准。
3. 将 PhyloBayes S5 consensus tree 与发表 FigS5 做关键拓扑和 posterior probability 比较；这是 PhyloBayes 拓扑复现最后缺口。
4. 整理 `results/MDGUI_dating/` 的 MCMCTree 拓展定年：把 `t_n41` 等 node ID 映射到具体类群节点。
5. 比较 `repeat1/summarization.out.txt` 与 `repeat2/summarization.out.txt` 的关键节点年龄和 95% HPD，判断重复运行是否足够一致。
6. 将 MCMCTree 的关键节点年龄与发表 FigS6 chronogram 做趋势层面的比较，但写成“拓展/近似”，不要写成原文严格复现。
7. 若继续追求严格 FigS6，确认服务器或本机是否有 PhyloBayes v4.1c / dating 版命令和 `readdiv`。
8. 查清 dating 版 PhyloBayes 的 fixed topology、fossil calibration、clock model cross-validation 输入格式。
9. 若严格 dating 工具可用，做最小化短测试，只验证输入格式、固定拓扑、calibration、clock/dating 命令能启动。
10. 若短测试通过，再决定是否做 LN / UGAM / strict clock cross-validation 和 final dating。
11. 无论是否严格重跑 PhyloBayes dating，都要整理发表 FigS6 chronogram 的关键节点年龄和 95% HPD，作为报告定年部分对照。
12. 写作阶段清楚区分 S5 PhyloBayes topology 复现、S6 原文 dating、以及 MCMCTree 快速替代/拓展。

## 最低可交付 FigS6 整理

如果 strict PhyloBayes dating 工具或时间不允许，最低可交付任务是整理发表 FigS6 chronogram：

- 读取 `published_trees/Delsuc-CurrBiol-2019_FigS6_PhyloBayes_chronogram_nexus_for_FigTree.tree`。
- 提取关键节点年龄和 `height_95%_HPD`。
- 将 HPD 从树文件的 `{上限, 下限}` 改写为报告中的 `下限-上限`。
- 明确写作口径为“整理发表 chronogram”，不是“本项目重跑 dating”。

需要整理的关键节点：

- Folivora 主要谱系起源。
- Caribbean sloths 早期分化。
- `Acratocnus + Parocnus`。
- `Choloepus + Mylodon`。
- `Bradypus` 与 `Megalonyx + Nothrotheriops` 相关分支。
- `Megalonyx + Nothrotheriops`。

已知示例：

```text
(Parocnus_serus_Lib54:29.2044,Acratocnus_ye_Lib58:29.2044)[&height_95%_HPD={38.4296,20.2786}]
```

解释为：

- 节点年龄：约 29.2044 Ma。
- 95% HPD：约 20.2786-38.4296 Ma。

## 需要避免的错误

- 不要把 S5 PhyloBayes MPI 拓扑复现写成 S6 dating 复现。
- 不要把 BEAST2 或 MCMCtree 结果写成原文 PhyloBayes dating。
- 不要把 substitutions-per-site branch lengths 当作 divergence times。
- 不要把 posterior probability 当作 bootstrap support。
- 不要把 FigS6 chronogram 整理写成自己重跑了 dating。
- 不要把当前 `results/MDGUI_dating/` 写成原文 PhyloBayes FigS6 严格复现；它是 PAML MCMCTree 拓展/近似定年。
- 不要忽略 ASDSF、ESS、PSRF 等收敛指标。
- 不要在 fossil calibration 格式不清楚时启动长时间 dating。
