"""
Publication-safe reproducibility script for the PLC security manuscript.
This code supports analysis and validation only.
"""

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

def relative_reduction(baseline: float, post: float) -> float:
    if baseline == 0:
        return 0.0
    return ((baseline - post) / baseline) * 100.0

def main():
    asr = pd.read_csv(ROOT / "data" / "processed" / "table5_asr.csv")
    mttr = pd.read_csv(ROOT / "data" / "processed" / "table6_mttr.csv")

    asr["Recomputed_Reduction_percent"] = asr.apply(
        lambda r: round(relative_reduction(r["ASR_Baseline_percent"], r["ASR_After_Mitigation_percent"]), 1), axis=1
    )
    mttr["Recomputed_Improvement_percent"] = mttr.apply(
        lambda r: round(relative_reduction(r["MTTR_Baseline_s"], r["MTTR_Post_Mitigation_s"]), 1), axis=1
    )

    out1 = ROOT / "results" / "recomputed_asr.csv"
    out2 = ROOT / "results" / "recomputed_mttr.csv"
    asr.to_csv(out1, index=False)
    mttr.to_csv(out2, index=False)

    print("Saved:", out1)
    print("Saved:", out2)
    print("\nASR")
    print(asr.to_string(index=False))
    print("\nMTTR")
    print(mttr.to_string(index=False))

if __name__ == "__main__":
    main()
