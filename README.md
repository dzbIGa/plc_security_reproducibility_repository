Interactive notebook can be added here if desired.
For journal submission, the script-based workflow is often more stable and easier to verify.

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
