# Reproducibility Package

This repository is directly associated with the research article:

**"Vulnerability Assessment and Mitigation for Siemens S7-1200 and S7-1500 PLCs in Industrial Networks"**

It provides all materials required to reproduce:

* the experimental workflow
* statistical analysis
* reported results and figures

The repository ensures full transparency and reproducibility of the study.

---

## Reproducibility statement

All results presented in the manuscript can be reproduced using the provided datasets and scripts.

The repository includes:

* full statistical workflow
* metric recalculation
* figure regeneration

---

## Repository structure

* `configs/` — example network and security configurations
* `data/processed/` — datasets corresponding to manuscript tables
* `data/synthetic/` — synthetic datasets for reproducibility
* `scripts/` — analysis, validation, and visualization scripts
* `docs/` — replication guide and documentation
* `results/` — generated outputs

---

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

All outputs will be saved in the `/results` directory.

---

## Quick verification

To quickly verify reproducibility:

python scripts/validate_tables.py

---

## Relation to the paper

This repository is not a generic code base.

It is a direct extension of the manuscript and contains the exact data structures and computational workflow used to generate the reported results.

---

## Included materials

### Configuration examples

* VLAN segmentation
* ACL policies
* IDS monitoring rules

### Data

* processed datasets aligned with manuscript tables
* synthetic datasets for statistical validation

### Scripts

* metric calculation
* statistical testing
* figure generation

---

## Citation

If you use this repository, please cite:

1. The journal article
2. The repository (Zenodo DOI)

---

## Security notice

This repository contains only anonymized and synthetic data.

No real industrial configurations, credentials, or sensitive network captures are included.

The materials are provided strictly for research reproducibility and educational purposes.

---

## Availability

GitHub repository:
https://github.com/dzbIGa/plc_security_reproducibility_repository

Zenodo DOI:
https://doi.org/10.5281/zenodo.19250402

---

## Ethical statement

The repository excludes sensitive operational data and does not contain any materials that could be used to compromise real industrial systems.

Its purpose is to support transparent, reproducible, and responsible cybersecurity research.
