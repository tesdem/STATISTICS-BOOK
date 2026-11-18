# Chapter 02: Asymmetric classification and capacity

## WHAT
In a simulated rare-event service, compare the review policies under transparent false-positive and false-negative costs.

## WHY
Cost-sensitive classification Figure 2.1 is accompanied by an age median (37), not a confusion matrix, expected-cost comparison or review-capacity analysis.

## HOW
Seeded synthetic data, an explicit diagnostic, and a reproducible figure; metrics exported to JSON.

**Notebook:** `chapter_02__asymmetric_classification_and_capacity.ipynb`

**Dataset used:** A seeded synthetic sample created at runtime in the notebook (seed = 20261024 + chapter number). No external source is loaded by the notebook.

**Optional supplied dataset mapping (not used in generated results):** adult.zip

## Detailed execution
1. Open a terminal in the repository root (the folder containing `requirements.txt`).
2. Create a Python 3.13 virtual environment and install `requirements.txt` (see root README).
3. Run `python scripts/run_all.py --chapter 2` for a fresh Jupyter-kernel execution.
4. Inspect `outputs/figures/chapter_02__asymmetric_classification_and_capacity.png` and `outputs/metrics/chapter_02__asymmetric_classification_and_capacity__metrics.json`.
5. Review `reports/execution_report.csv` for the outcome and any failure.
6. For manual Jupyter execution, launch from the repository root; use the Python kernel created in your virtual environment, then select **Restart & Run All**.

## Interpret the figure
The figure is a diagnostic for **asymmetric classification and capacity**, not an empirical population conclusion. Compare the plotted labels with the saved metric JSON and rerun with a different seed to assess sensitivity.

## Limitations and scientific validity
A cost-sensitive policy can improve simulated expected loss; real utility and fairness need elicited costs and validation.

Successful execution checks Python dependencies, output generation, and internal numerical flow. It does **not** independently validate assumptions, identification, model selection, data provenance, causal interpretation, fairness or real-world predictive usefulness.
