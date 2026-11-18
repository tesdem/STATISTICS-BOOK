# Chapter 28: Observed-data causal adjustment

## WHAT
Cross-fit propensity and outcome learners to estimate a synthetic treatment effect using observed covariates only.

## WHY
The manuscript retains old Figure 28.1 alongside supplemental Figure 28.2 and reports revised non-oracle causal analyses; no independent reconciliation of old and replacement notebook figures is shown.

## HOW
Seeded synthetic data, an explicit diagnostic, and a reproducible figure; metrics exported to JSON.

**Notebook:** `chapter_28__observed_data_causal_adjustment.ipynb`

**Dataset used:** A seeded synthetic sample created at runtime in the notebook (seed = 20261024 + chapter number). No external source is loaded by the notebook.

**Optional supplied dataset mapping (not used in generated results):** bank+marketing.zip

## Detailed execution
1. Open a terminal in the repository root (the folder containing `requirements.txt`).
2. Create a Python 3.13 virtual environment and install `requirements.txt` (see root README).
3. Run `python scripts/run_all.py --chapter 28` for a fresh Jupyter-kernel execution.
4. Inspect `outputs/figures/chapter_28__observed_data_causal_adjustment.png` and `outputs/metrics/chapter_28__observed_data_causal_adjustment__metrics.json`.
5. Review `reports/execution_report.csv` for the outcome and any failure.
6. For manual Jupyter execution, launch from the repository root; use the Python kernel created in your virtual environment, then select **Restart & Run All**.

## Interpret the figure
The figure is a diagnostic for **observed-data causal adjustment**, not an empirical population conclusion. Compare the plotted labels with the saved metric JSON and rerun with a different seed to assess sensitivity.

## Limitations and scientific validity
Unmeasured confounding remains a threat; simulated truth is evaluation-only, never estimator input.

Successful execution checks Python dependencies, output generation, and internal numerical flow. It does **not** independently validate assumptions, identification, model selection, data provenance, causal interpretation, fairness or real-world predictive usefulness.
