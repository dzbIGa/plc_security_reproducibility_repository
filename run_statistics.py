"""
Publication-safe reproducibility script for the PLC security manuscript.
This code supports analysis and validation only.
"""

from pathlib import Path
import pandas as pd
from scipy import stats
import numpy as np

ROOT = Path(__file__).resolve().parents[1]

def cohens_d_paired(a, b):
    diff = np.array(a) - np.array(b)
    sd = diff.std(ddof=1)
    if sd == 0:
        return float("inf") if diff.mean() != 0 else 0.0
    return diff.mean() / sd

def ci95(diff):
    diff = np.array(diff)
    n = len(diff)
    mean = diff.mean()
    se = diff.std(ddof=1) / np.sqrt(n)
    tcrit = stats.t.ppf(0.975, df=n-1)
    lo = mean - tcrit * se
    hi = mean + tcrit * se
    return lo, hi

def paired_report(path, value_col):
    df = pd.read_csv(path)
    rows = []
    for scenario in df["Scenario"].unique():
        sub = df[df["Scenario"] == scenario]
        a = sub[sub["Condition"] == "Baseline"][value_col].tolist()
        b = sub[sub["Condition"] == "PostMitigation"][value_col].tolist()
        t, p = stats.ttest_rel(a, b)
        diff = np.array(b) - np.array(a)
        lo, hi = ci95(diff)
        d = cohens_d_paired(a, b)
        rows.append({
            "Scenario": scenario,
            "Mean_Difference_PostMinusBaseline": round(float(np.mean(diff)), 3),
            "t_value": round(float(t), 5),
            "p_value": float(p),
            "CI95_PostMinusBaseline": f"[{lo:.3f}, {hi:.3f}]",
            "Cohens_d_paired": round(float(d), 3) if np.isfinite(d) else "inf"
        })
    return pd.DataFrame(rows)

def main():
    reports = {
        "asr": paired_report(ROOT / "data" / "synthetic" / "synthetic_asr_trials.csv", "ASR_percent"),
        "mttr": paired_report(ROOT / "data" / "synthetic" / "synthetic_mttr_trials.csv", "MTTR_s"),
        "traffic": paired_report(ROOT / "data" / "synthetic" / "synthetic_traffic_trials.csv", "Packets_per_sec"),
    }
    for name, df in reports.items():
        out = ROOT / "results" / f"statistics_{name}.csv"
        df.to_csv(out, index=False)
        print(f"Saved {out}")
        print(df.to_string(index=False))
        print()

if __name__ == "__main__":
    main()
