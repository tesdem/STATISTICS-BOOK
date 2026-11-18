# Chapter 46: Tail modelling stress check

## WHAT
Fit a generalized Pareto model above a fixed high threshold and inspect threshold sensitivity.

## WHY
Extreme-value stress-testing caption is supported only by a descriptive q95 1.558 and tail count 50, not tail modelling.

## HOW
Seeded synthetic data, an explicit diagnostic, and a reproducible figure; metrics exported to JSON.

**Notebook:** `chapter_46__tail_modelling_stress_check.ipynb`

**Dataset used:** A seeded synthetic sample created at runtime in the notebook (seed = 20261024 + chapter number). No external source is loaded by the notebook.

**Optional supplied dataset mapping (not used in generated results):** No chapter-specific external dataset supplied.

## Detailed execution
1. Open a terminal in the repository root (the folder containing `requirements.txt`).
2. Create a Python 3.13 virtual environment and install `requirements.txt` (see root README).
3. Run `python scripts/run_all.py --chapter 46` for a fresh Jupyter-kernel execution.
4. Inspect `outputs/figures/chapter_46__tail_modelling_stress_check.png` and `outputs/metrics/chapter_46__tail_modelling_stress_check__metrics.json`.
5. Review `reports/execution_report.csv` for the outcome and any failure.
6. For manual Jupyter execution, launch from the repository root; use the Python kernel created in your virtual environment, then select **Restart & Run All**.

## Interpret the figure
The figure is a diagnostic for **tail modelling stress check**, not an empirical population conclusion. Compare the plotted labels with the saved metric JSON and rerun with a different seed to assess sensitivity.

## Limitations and scientific validity
Tail extrapolation is unstable with few extremes; the model needs independent verification.

Successful execution checks Python dependencies, output generation, and internal numerical flow. It does **not** independently validate assumptions, identification, model selection, data provenance, causal interpretation, fairness or real-world predictive usefulness.
