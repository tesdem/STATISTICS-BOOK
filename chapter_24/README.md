# Chapter 24 — Frequentist and Bayesian Inference: Two Languages of Evidence

Notebook: `chapter_24__bayesian_beta_binomial_prior_sensitivity.ipynb`

## WHAT
This laboratory explores **bayesian beta binomial prior sensitivity**, focusing on: Frequentist and Bayesian inference provide different but legitimate descriptions of uncertainty; transparent modelling, sensitivity to assumptions, and clear interpretation matter more than allegiance to a methodological label.

## WHY
It provides a controlled teaching example of the chapter's main evidential distinction. The data are **realistic but synthetic**; no uploaded observational dataset or external source is used in this specific lab.

## HOW
From the repository root, run:

```bash
python -m pip install -r requirements.txt
python scripts/run_all.py --chapter 24
```

For Chapter 32A, `--chapter 32A` executes all three distinct Chapter 32A laboratories. You may also open the notebook and choose Restart & Run All. It writes a generated dataset CSV, JSON metrics and named PNG figure to repository-relative paths.

## Inputs and outputs
- Input: transparent seeded synthetic generation in `scripts/new_labs_engine.py`, code key `24`.
- Dataset: `datasets/generated/chapter_24__bayesian_beta_binomial_prior_sensitivity__synthetic.csv`
- Figure: `outputs/figures/chapter_24__bayesian_beta_binomial_prior_sensitivity.png`
- Metrics: `outputs/metrics/chapter_24__bayesian_beta_binomial_prior_sensitivity.json`
- Tested notebook: `outputs/executed_notebooks/chapter_24__bayesian_beta_binomial_prior_sensitivity.ipynb`

## Interpretation, validation, and limits
The validation cell checks execution artifacts and the number of generated observations. Examine method-specific numeric metrics and analytical assumptions before drawing scientific conclusions. Execution of synthetic examples is not a substitute for expert methodological review.
