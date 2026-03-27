"""
Publication-safe reproducibility script for the PLC security manuscript.
This code supports analysis and validation only.
"""

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

def approx_equal(a, b, tol=0.2):
    return abs(a - b) <= tol

def main():
    asr = pd.read_csv(ROOT / "data" / "processed" / "table5_asr.csv")
    mttr = pd.read_csv(ROOT / "data" / "processed" / "table6_mttr.csv")
    traffic = pd.read_csv(ROOT / "data" / "processed" / "figure2_traffic_volume.csv")

    assert len(asr) == 4, "Expected 4 ASR scenarios"
    assert len(mttr) == 4, "Expected 4 MTTR scenarios"
    assert len(traffic) == 4, "Expected 4 traffic scenarios"

    # manuscript consistency checks
    expected_asr = {
        "Replay Attack (Stop PLC)": 100.0,
        "Brute-force Login": 87.5,
        "Unauthorized Firmware Upload": 85.7,
        "Configuration Dump": 100.0,
    }
    for _, row in asr.iterrows():
        calc = round(((row["ASR_Baseline_percent"] - row["ASR_After_Mitigation_percent"]) / row["ASR_Baseline_percent"]) * 100, 1)
        assert approx_equal(calc, expected_asr[row["Attack Type"]]), f"ASR mismatch for {row['Attack Type']}"

    expected_mttr = {
        "Replay Attack": 100.0,
        "Brute-force Login": 61.1,
        "Firmware Upload": 63.6,
        "Configuration Dump": 100.0,
    }
    for _, row in mttr.iterrows():
        calc = round(((row["MTTR_Baseline_s"] - row["MTTR_Post_Mitigation_s"]) / row["MTTR_Baseline_s"]) * 100, 1)
        assert approx_equal(calc, expected_mttr[row["Scenario"]]), f"MTTR mismatch for {row['Scenario']}"

    print("All publication-safe consistency checks passed.")

if __name__ == "__main__":
    main()
