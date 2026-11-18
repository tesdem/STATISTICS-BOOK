# Chapter 41: Sensor drift and measurement missingness

## WHAT
Inject drift and missing observations into a sensor series and evaluate summary distortion.

## WHY
Sensor missingness/drift illustration and schematic counterfactual trend cannot support causal cross-domain claims.

## HOW
Seeded synthetic data, an explicit diagnostic, and a reproducible figure; metrics exported to JSON.

**Notebook:** `chapter_41__sensor_drift_and_measurement_missingness.ipynb`

**Dataset used:** A seeded synthetic sample created at runtime in the notebook (seed = 20261024 + chapter number). No external source is loaded by the notebook.

**Optional supplied dataset mapping (not used in generated results):** air+quality.zip

## Detailed execution
1. Open a terminal in the repository root (the folder containing `requirements.txt`).
2. Create a Python 3.13 virtual environment and install `requirements.txt` (see root README).
3. Run `python scripts/run_all.py --chapter 41` for a fresh Jupyter-kernel execution.
4. Inspect `outputs/figures/chapter_41__sensor_drift_and_measurement_missingness.png` and `outputs/metrics/chapter_41__sensor_drift_and_measurement_missingness__metrics.json`.
5. Review `reports/execution_report.csv` for the outcome and any failure.
6. For manual Jupyter execution, launch from the repository root; use the Python kernel created in your virtual environment, then select **Restart & Run All**.

## Interpret the figure
The figure is a diagnostic for **sensor drift and measurement missingness**, not an empirical population conclusion. Compare the plotted labels with the saved metric JSON and rerun with a different seed to assess sensitivity.

## Limitations and scientific validity
No causal transfer across scientific fields is established.

Successful execution checks Python dependencies, output generation, and internal numerical flow. It does **not** independently validate assumptions, identification, model selection, data provenance, causal interpretation, fairness or real-world predictive usefulness.
