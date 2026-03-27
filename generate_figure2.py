"""
Publication-safe reproducibility script for the PLC security manuscript.
This code supports analysis and validation only.
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]

def main():
    df = pd.read_csv(ROOT / "data" / "processed" / "figure2_traffic_volume.csv")
    x = np.arange(len(df))
    width = 0.36

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(x - width/2, df["Baseline_packets_per_sec"], width, label="Baseline")
    ax.bar(x + width/2, df["Post_Mitigation_packets_per_sec"], width, label="Post-mitigation")

    ax.set_xticks(x)
    ax.set_xticklabels(df["Scenario"], rotation=20, ha="right")
    ax.set_ylabel("Packets per second")
    ax.set_title("Network traffic volume reduction pre- and post-mitigation")
    ax.legend()
    plt.tight_layout()

    out = ROOT / "results" / "figure2_regenerated.png"
    fig.savefig(out, dpi=300)
    print(f"Saved {out}")

if __name__ == "__main__":
    main()
