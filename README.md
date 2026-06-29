# Walmart Sales Analysis

Professional Python project for Walmart sales analysis. The original notebook is preserved, and reusable project code now lives in `src/walmart_analytics/`.

## Staff Data Engineer assessment

This is a solid business analytics repository for a junior data role because it uses retail data and operational metrics. The main gap was that the project was notebook-only and lacked a reproducible Python structure.

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

## How to run

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m pytest
python -m walmart_analytics.pipeline --input data/raw/Walmart.csv --output data/processed
```

## What the pipeline provides

- CSV/Excel ingestion with error handling.
- Column normalization.
- Missing-value summary.
- Numeric profiling.
- Duplicate-row metrics.
- Generated artifacts in `data/processed/`.

## Current limitations

- The raw dataset is not committed.
- Business-specific aggregations from the notebook should be moved into tested Python functions.
- A SQL layer for store/week level metrics would make the project stronger for Analytics Engineering roles.
