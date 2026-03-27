# Data Dictionary

## table5_asr.csv
- `Attack Type`: evaluated scenario
- `ASR_Baseline_percent`: attack success rate before mitigation
- `ASR_After_Mitigation_percent`: attack success rate after mitigation
- `Reduction_percent`: relative reduction

## table6_mttr.csv
- `Scenario`: evaluated scenario
- `MTTR_Baseline_s`: mean time to recovery in seconds before mitigation
- `MTTR_Post_Mitigation_s`: MTTR after mitigation
- `Improvement_percent`: relative reduction

## table7_statistics.csv
- `Metric`: ASR, MTTR, or Traffic Volume
- `Scenario`: evaluated scenario
- `Mean_Difference`: post minus baseline or reported manuscript difference
- `t_value`: paired t-test statistic
- `p_value`: exact p-value
- `CI_95`: 95% confidence interval
- `Cohens_d`: effect size

## synthetic_*_trials.csv
Synthetic repeated-trial data used only to demonstrate the analysis workflow.
They are not raw industrial captures.
