# Chapter 47: Decision thresholds and monitoring

## WHAT
Evaluate false alarms, missed events and expected costs under model degradation.

## WHY
Monitoring/decision-threshold laboratory repeats capacity-series error MAE 1648, worse than baseline 1504; action-value evidence is absent.

## HOW
Seeded synthetic data, an explicit diagnostic, and a reproducible figure; metrics exported to JSON.

**Notebook:** `chapter_47__decision_thresholds_and_monitoring.ipynb`

**Dataset used:** A seeded synthetic sample created at runtime in the notebook (seed = 20261024 + chapter number). No external source is loaded by the notebook.

**Optional supplied dataset mapping (not used in generated results):** bike+sharing+dataset.zip

## Detailed execution
1. Open a terminal in the repository root (the folder containing `requirements.txt`).
2. Create a Python 3.13 virtual environment and install `requirements.txt` (see root README).
3. Run `python scripts/run_all.py --chapter 47` for a fresh Jupyter-kernel execution.
4. Inspect `outputs/figures/chapter_47__decision_thresholds_and_monitoring.png` and `outputs/metrics/chapter_47__decision_thresholds_and_monitoring__metrics.json`.
5. Review `reports/execution_report.csv` for the outcome and any failure.
6. For manual Jupyter execution, launch from the repository root; use the Python kernel created in your virtual environment, then select **Restart & Run All**.

## Interpret the figure
The figure is a diagnostic for **decision thresholds and monitoring**, not an empirical population conclusion. Compare the plotted labels with the saved metric JSON and rerun with a different seed to assess sensitivity.

## Limitations and scientific validity
The result does not establish real-world action benefit or a causal policy effect.

Successful execution checks Python dependencies, output generation, and internal numerical flow. It does **not** independently validate assumptions, identification, model selection, data provenance, causal interpretation, fairness or real-world predictive usefulness.
