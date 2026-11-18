# Chapter 20: Count model dispersion

## WHAT
Compare Poisson variance predictions with overdispersed synthetic counts.

## WHY
Count-distribution laboratory reports median 366, not distribution-fit or dispersion evidence.

## HOW
Seeded synthetic data, an explicit diagnostic, and a reproducible figure; metrics exported to JSON.

**Notebook:** `chapter_20__count_model_dispersion.ipynb`

**Dataset used:** A seeded synthetic sample created at runtime in the notebook (seed = 20261024 + chapter number). No external source is loaded by the notebook.

**Optional supplied dataset mapping (not used in generated results):** bike+sharing+dataset.zip

## Detailed execution
1. Open a terminal in the repository root (the folder containing `requirements.txt`).
2. Create a Python 3.13 virtual environment and install `requirements.txt` (see root README).
3. Run `python scripts/run_all.py --chapter 20` for a fresh Jupyter-kernel execution.
4. Inspect `outputs/figures/chapter_20__count_model_dispersion.png` and `outputs/metrics/chapter_20__count_model_dispersion__metrics.json`.
5. Review `reports/execution_report.csv` for the outcome and any failure.
6. For manual Jupyter execution, launch from the repository root; use the Python kernel created in your virtual environment, then select **Restart & Run All**.

## Interpret the figure
The figure is a diagnostic for **count model dispersion**, not an empirical population conclusion. Compare the plotted labels with the saved metric JSON and rerun with a different seed to assess sensitivity.

## Limitations and scientific validity
Overdispersion suggests model review; it does not uniquely identify a negative-binomial process.

Successful execution checks Python dependencies, output generation, and internal numerical flow. It does **not** independently validate assumptions, identification, model selection, data provenance, causal interpretation, fairness or real-world predictive usefulness.
