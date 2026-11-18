# Chapter 40: Institutional indicator traceability

## WHAT
Compute linked indicator rates with explicit denominators and missingness checks.

## WHY
Institutional-indicator figure reports 20,000 valid TIME_PERIOD values; this demonstrates completeness, not policy/institutional intelligence.

## HOW
Seeded synthetic data, an explicit diagnostic, and a reproducible figure; metrics exported to JSON.

**Notebook:** `chapter_40__institutional_indicator_traceability.ipynb`

**Dataset used:** A seeded synthetic sample created at runtime in the notebook (seed = 20261024 + chapter number). No external source is loaded by the notebook.

**Optional supplied dataset mapping (not used in generated results):** GI_AII.csv

## Detailed execution
1. Open a terminal in the repository root (the folder containing `requirements.txt`).
2. Create a Python 3.13 virtual environment and install `requirements.txt` (see root README).
3. Run `python scripts/run_all.py --chapter 40` for a fresh Jupyter-kernel execution.
4. Inspect `outputs/figures/chapter_40__institutional_indicator_traceability.png` and `outputs/metrics/chapter_40__institutional_indicator_traceability__metrics.json`.
5. Review `reports/execution_report.csv` for the outcome and any failure.
6. For manual Jupyter execution, launch from the repository root; use the Python kernel created in your virtual environment, then select **Restart & Run All**.

## Interpret the figure
The figure is a diagnostic for **institutional indicator traceability**, not an empirical population conclusion. Compare the plotted labels with the saved metric JSON and rerun with a different seed to assess sensitivity.

## Limitations and scientific validity
Synthetic lineage illustrates governance but not genuine policy effectiveness.

Successful execution checks Python dependencies, output generation, and internal numerical flow. It does **not** independently validate assumptions, identification, model selection, data provenance, causal interpretation, fairness or real-world predictive usefulness.
