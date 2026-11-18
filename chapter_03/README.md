# Chapter 03 — The Language of Statistical Reasoning

Notebook: `chapter_03__repeated_visits_clustered_uncertainty.ipynb`

## WHAT
This laboratory explores **repeated visits clustered uncertainty**, focusing on: Precise statistical vocabulary determines what can legitimately be inferred.

## WHY
It provides a controlled teaching example of the chapter's main evidential distinction. The data are **realistic but synthetic**; no uploaded observational dataset or external source is used in this specific lab.

## HOW
From the repository root, run:

```bash
python -m pip install -r requirements.txt
python scripts/run_all.py --chapter 03
```

For Chapter 32A, `--chapter 32A` executes all three distinct Chapter 32A laboratories. You may also open the notebook and choose Restart & Run All. It writes a generated dataset CSV, JSON metrics and named PNG figure to repository-relative paths.

## Inputs and outputs
- Input: transparent seeded synthetic generation in `scripts/new_labs_engine.py`, code key `03`.
- Dataset: `datasets/generated/chapter_03__repeated_visits_clustered_uncertainty__synthetic.csv`
- Figure: `outputs/figures/chapter_03__repeated_visits_clustered_uncertainty.png`
- Metrics: `outputs/metrics/chapter_03__repeated_visits_clustered_uncertainty.json`
- Tested notebook: `outputs/executed_notebooks/chapter_03__repeated_visits_clustered_uncertainty.ipynb`

## Interpretation, validation, and limits
The validation cell checks execution artifacts and the number of generated observations. Examine method-specific numeric metrics and analytical assumptions before drawing scientific conclusions. Execution of synthetic examples is not a substitute for expert methodological review.
