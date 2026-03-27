
This repository is directly associated with the research article:

"Vulnerability Assessment and Mitigation for Siemens S7-1200 and S7-1500 PLCs in Industrial Networks"

The repository provides all materials necessary to reproduce the experimental workflow, statistical analysis, and reported results.Interactive notebook can be added here if desired.
For journal submission, the script-based workflow is often more stable and easier to verify.

## Citation

If you use this repository, please cite:

1. The journal article
2. This repository (Zenodo DOI)

This ensures proper attribution of the research work.

## Security Notice

This repository contains only anonymized and synthetic data.

No real industrial configurations, credentials, or sensitive network captures are included.

The materials are provided strictly for research reproducibility and educational purposes.

## Reproducibility instructions

To reproduce the main results:

1. Install dependencies:
pip install -r requirements.txt

2. Recalculate metrics:
python scripts/calculate_metrics.py

3. Run statistical validation:
python scripts/run_statistics.py

4. Generate Figure 2:
python scripts/generate_figure2.py

All outputs will be saved in the /results directory.
