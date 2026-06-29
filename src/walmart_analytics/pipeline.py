from __future__ import annotations

import argparse
import json
import logging
from pathlib import Path
from typing import Any, Sequence

import pandas as pd

LOGGER = logging.getLogger(__name__)
PROJECT_NAME = "Walmart sales analysis"


class DataValidationError(ValueError):
    """Raised when the input dataset is not usable by the pipeline."""


def normalize_column_name(column: object) -> str:
    """Normalize a source column name for Python and SQL-friendly usage."""
    return str(column).strip().lower().replace(" ", "_").replace("-", "_")


def load_dataset(path: str | Path, required_columns: Sequence[str] = ()) -> pd.DataFrame:
    """Load CSV or Excel data, normalize columns and validate required fields."""
    dataset_path = Path(path)
    if not dataset_path.exists():
        raise FileNotFoundError(f"Dataset not found: {dataset_path}")
    suffix = dataset_path.suffix.lower()
    LOGGER.info("Loading dataset from %s", dataset_path)
    if suffix == ".csv":
        df = pd.read_csv(dataset_path)
    elif suffix in {".xlsx", ".xls"}:
        df = pd.read_excel(dataset_path)
    else:
        raise DataValidationError(f"Unsupported file format: {suffix}")
    df = df.copy()
    df.columns = [normalize_column_name(column) for column in df.columns]
    missing = sorted(set(required_columns) - set(df.columns))
    if missing:
        raise DataValidationError(f"Missing required columns: {missing}")
    return df


def profile_dataset(df: pd.DataFrame) -> dict[str, Any]:
    """Return high-level quality metrics for a dataframe."""
    return {"row_count": int(len(df)), "column_count": int(df.shape[1]), "duplicate_rows": int(df.duplicated().sum())}


def missing_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Return missing-value count and percentage by column."""
    total_rows = len(df)
    summary = pd.DataFrame({"column": df.columns, "missing_count": df.isna().sum().values})
    summary["missing_pct"] = 0.0 if total_rows == 0 else summary["missing_count"] / total_rows
    return summary.sort_values(["missing_count", "column"], ascending=[False, True]).reset_index(drop=True)


def sales_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Return Walmart sales summaries when expected sales columns are available."""
    if "weekly_sales" not in df.columns:
        LOGGER.info("Skipping sales summary; missing optional column: weekly_sales")
        return pd.DataFrame()
    if "store" in df.columns:
        return (
            df.groupby("store", dropna=False)
            .agg(records=("weekly_sales", "size"), avg_weekly_sales=("weekly_sales", "mean"), total_weekly_sales=("weekly_sales", "sum"))
            .reset_index()
            .sort_values("total_weekly_sales", ascending=False)
        )
    return pd.DataFrame(
        {"metric": ["records", "avg_weekly_sales", "total_weekly_sales"], "value": [int(len(df)), float(df["weekly_sales"].mean()), float(df["weekly_sales"].sum())]}
    )


def run_pipeline(input_path: str | Path, output_dir: str | Path = "data/processed") -> dict[str, Any]:
    """Run local profiling and optional Walmart sales summaries for an available dataset."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    df = load_dataset(input_path)
    metrics = profile_dataset(df)
    missing_summary(df).to_csv(output_path / "missing_summary.csv", index=False)
    df.select_dtypes(include="number").describe().transpose().to_csv(output_path / "numeric_summary.csv")
    sales = sales_summary(df)
    if not sales.empty:
        sales.to_csv(output_path / "sales_summary.csv", index=False)
    (output_path / "dataset_metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    LOGGER.info("Pipeline completed for %s", PROJECT_NAME)
    return {"rows": metrics["row_count"], "outputs": str(output_path)}


def main(argv: Sequence[str] | None = None) -> int:
    """CLI entrypoint."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s")
    parser = argparse.ArgumentParser(description=PROJECT_NAME)
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", default="data/processed")
    args = parser.parse_args(argv)
    try:
        print(json.dumps(run_pipeline(args.input, args.output), indent=2))
    except Exception:
        LOGGER.exception("Pipeline failed")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
