# Chapter 45: Shift, uncertainty and abstention

## WHAT
Test probability calibration and selective accuracy under covariate shift.

## WHY
One synthetic transportability holdout MAE 0.8338 versus baseline 1.561 does not show reliability under actual deployment shift.

## HOW
Seeded synthetic data, an explicit diagnostic, and a reproducible figure; metrics exported to JSON.

**Notebook:** `chapter_45__shift_uncertainty_and_abstention.ipynb`

**Dataset used:** A seeded synthetic sample created at runtime in the notebook (seed = 20261024 + chapter number). No external source is loaded by the notebook.

**Optional supplied dataset mapping (not used in generated results):** No chapter-specific external dataset supplied.

## Detailed execution
1. Open a terminal in the repository root (the folder containing `requirements.txt`).
2. Create a Python 3.13 virtual environment and install `requirements.txt` (see root README).
3. Run `python scripts/run_all.py --chapter 45` for a fresh Jupyter-kernel execution.
4. Inspect `outputs/figures/chapter_45__shift_uncertainty_and_abstention.png` and `outputs/metrics/chapter_45__shift_uncertainty_and_abstention__metrics.json`.
5. Review `reports/execution_report.csv` for the outcome and any failure.
6. For manual Jupyter execution, launch from the repository root; use the Python kernel created in your virtual environment, then select **Restart & Run All**.

## Interpret the figure
The figure is a diagnostic for **shift, uncertainty and abstention**, not an empirical population conclusion. Compare the plotted labels with the saved metric JSON and rerun with a different seed to assess sensitivity.

## Limitations and scientific validity
Transportability outside the simulated shifts remains unverified.

Successful execution checks Python dependencies, output generation, and internal numerical flow. It does **not** independently validate assumptions, identification, model selection, data provenance, causal interpretation, fairness or real-world predictive usefulness.
