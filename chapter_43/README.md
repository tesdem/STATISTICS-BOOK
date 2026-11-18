# Chapter 43: Joined indicators and provenance

## WHAT
Join simulated institutional indicators by period and entity and monitor reconciliation mismatches.

## WHY
Indicator-integration Figure 43.1 reports TIME_PERIOD completeness only, not shared institutional intelligence or decision integration.

## HOW
Seeded synthetic data, an explicit diagnostic, and a reproducible figure; metrics exported to JSON.

**Notebook:** `chapter_43__joined_indicators_and_provenance.ipynb`

**Dataset used:** A seeded synthetic sample created at runtime in the notebook (seed = 20261024 + chapter number). No external source is loaded by the notebook.

**Optional supplied dataset mapping (not used in generated results):** GI_AII.csv

## Detailed execution
1. Open a terminal in the repository root (the folder containing `requirements.txt`).
2. Create a Python 3.13 virtual environment and install `requirements.txt` (see root README).
3. Run `python scripts/run_all.py --chapter 43` for a fresh Jupyter-kernel execution.
4. Inspect `outputs/figures/chapter_43__joined_indicators_and_provenance.png` and `outputs/metrics/chapter_43__joined_indicators_and_provenance__metrics.json`.
5. Review `reports/execution_report.csv` for the outcome and any failure.
6. For manual Jupyter execution, launch from the repository root; use the Python kernel created in your virtual environment, then select **Restart & Run All**.

## Interpret the figure
The figure is a diagnostic for **joined indicators and provenance**, not an empirical population conclusion. Compare the plotted labels with the saved metric JSON and rerun with a different seed to assess sensitivity.

## Limitations and scientific validity
An integrated table is not automatically shared institutional intelligence.

Successful execution checks Python dependencies, output generation, and internal numerical flow. It does **not** independently validate assumptions, identification, model selection, data provenance, causal interpretation, fairness or real-world predictive usefulness.
