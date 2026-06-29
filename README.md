# Walmart Sales Analysis

This repository contains the original Walmart sales notebook and a new lightweight Python profiling layer under `src/walmart_analytics/`.

## What this PR changes

The notebook remains the source of the full exploratory analysis. The Python code added here does not recreate every chart or business question. It provides:

- local CSV/Excel ingestion with explicit errors;
- normalized column names;
- missing-value and numeric profiling outputs;
- duplicate-row metrics;
- an optional `sales_summary.csv` when `weekly_sales` is present;
- tests for ingestion and profiling behavior.

## Structure

```text
.
├── Walmart.ipynb
├── data/
├── images/
├── notebooks/
├── src/walmart_analytics/
├── tests/
├── requirements.txt
└── README.md
```

## Dataset requirement

The expected local input is `data/raw/Walmart.csv`. That file is not committed. Without it, the project pipeline cannot be executed end to end.

## How to run when the dataset is available

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m pytest
python -m walmart_analytics.pipeline --input data/raw/Walmart.csv --output data/processed
```

## Outputs

Always generated when the input file exists:

- `data/processed/missing_summary.csv`
- `data/processed/numeric_summary.csv`
- `data/processed/dataset_metrics.json`

Generated only when expected sales columns exist:

- `data/processed/sales_summary.csv`

## Current limitations

- Business-specific aggregations from the notebook are not fully extracted yet.
- No SQL layer or dashboard is added in this PR.
- The README avoids claiming reproducibility beyond the dataset-dependent profiling command.
