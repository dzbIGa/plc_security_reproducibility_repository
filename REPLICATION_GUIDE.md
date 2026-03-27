# Replication Guide

## Scope
This guide explains how to reproduce the published **analysis pipeline** and the mitigation-evaluation workflow
using the publication-safe materials included in this package.

## Step 1 — Prepare environment
Install dependencies:
```bash
pip install -r requirements.txt
```

## Step 2 — Validate manuscript tables
```bash
python scripts/validate_tables.py
```

## Step 3 — Recompute percentage improvements
```bash
python scripts/calculate_metrics.py
```

## Step 4 — Re-run statistics
```bash
python scripts/run_statistics.py
```

## Step 5 — Regenerate Figure 2
```bash
python scripts/generate_figure2.py
```

## Shared materials
- synthetic trial data reproduce the statistical workflow without disclosing sensitive pcap files;
- processed CSV files mirror the tables reported in the manuscript;
- config examples document the security architecture and post-mitigation controls in a publication-safe form.

## What is intentionally excluded
- offensive exploit scripts
- real plant identifiers
- raw packet captures from sensitive environments
- secrets, credentials, certificates, or production exports
