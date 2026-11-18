# Chapter 38 — Ethics, Fairness, Privacy and the Responsibilities of Statistical Practice

Notebook: `chapter_38__group_fairness_and_sparse_sample_uncertainty.ipynb`

## WHAT
This laboratory explores **group fairness and sparse sample uncertainty**, focusing on: Technically correct statistical calculations may still be unethical when data collection, representation, decisions, or downstream impacts violate legitimate interests. Ethical statistics requires attention to how evidence is produced, interpreted, and used.

## WHY
It provides a controlled teaching example of the chapter's main evidential distinction. The data are **realistic but synthetic**; no uploaded observational dataset or external source is used in this specific lab.

## HOW
From the repository root, run:

```bash
python -m pip install -r requirements.txt
python scripts/run_all.py --chapter 38
```

For Chapter 32A, `--chapter 32A` executes all three distinct Chapter 32A laboratories. You may also open the notebook and choose Restart & Run All. It writes a generated dataset CSV, JSON metrics and named PNG figure to repository-relative paths.

## Inputs and outputs
- Input: transparent seeded synthetic generation in `scripts/new_labs_engine.py`, code key `38`.
- Dataset: `datasets/generated/chapter_38__group_fairness_and_sparse_sample_uncertainty__synthetic.csv`
- Figure: `outputs/figures/chapter_38__group_fairness_and_sparse_sample_uncertainty.png`
- Metrics: `outputs/metrics/chapter_38__group_fairness_and_sparse_sample_uncertainty.json`
- Tested notebook: `outputs/executed_notebooks/chapter_38__group_fairness_and_sparse_sample_uncertainty.ipynb`

## Interpretation, validation, and limits
The validation cell checks execution artifacts and the number of generated observations. Examine method-specific numeric metrics and analytical assumptions before drawing scientific conclusions. Execution of synthetic examples is not a substitute for expert methodological review.
