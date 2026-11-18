# Chapter 23: Type-I error and statistical power

## WHAT
Evaluate a Welch test under null and alternative scenarios with multiple-testing context.

## WHY
The hypothesis-testing chapter reports a descriptive median (9.06e+05) as laboratory result rather than test-size, power or assumption checks.

## HOW
Seeded synthetic data, an explicit diagnostic, and a reproducible figure; metrics exported to JSON.

**Notebook:** `chapter_23__type_i_error_and_statistical_power.ipynb`

**Dataset used:** A seeded synthetic sample created at runtime in the notebook (seed = 20261024 + chapter number). No external source is loaded by the notebook.

**Optional supplied dataset mapping (not used in generated results):** breast+cancer+wisconsin+diagnostic.zip

## Detailed execution
1. Open a terminal in the repository root (the folder containing `requirements.txt`).
2. Create a Python 3.13 virtual environment and install `requirements.txt` (see root README).
3. Run `python scripts/run_all.py --chapter 23` for a fresh Jupyter-kernel execution.
4. Inspect `outputs/figures/chapter_23__type_i_error_and_statistical_power.png` and `outputs/metrics/chapter_23__type_i_error_and_statistical_power__metrics.json`.
5. Review `reports/execution_report.csv` for the outcome and any failure.
6. For manual Jupyter execution, launch from the repository root; use the Python kernel created in your virtual environment, then select **Restart & Run All**.

## Interpret the figure
The figure is a diagnostic for **type-i error and statistical power**, not an empirical population conclusion. Compare the plotted labels with the saved metric JSON and rerun with a different seed to assess sensitivity.

## Limitations and scientific validity
Monte Carlo accuracy is finite; validity requires the test assumptions.

Successful execution checks Python dependencies, output generation, and internal numerical flow. It does **not** independently validate assumptions, identification, model selection, data provenance, causal interpretation, fairness or real-world predictive usefulness.
