# Chapter 34 — Statistics, Data Science and Machine Learning: Learning from Data

Notebook: `chapter_34__prediction_leakage_and_temporal_shift.ipynb`

## WHAT
This laboratory explores **prediction leakage and temporal shift**, focusing on: Reliable machine learning is a disciplined predictive experiment: define the task, prevent leakage, evaluate on relevant unseen data, measure uncertainty, and distinguish prediction from intervention.

## WHY
It provides a controlled teaching example of the chapter's main evidential distinction. The data are **realistic but synthetic**; no uploaded observational dataset or external source is used in this specific lab.

## HOW
From the repository root, run:

```bash
python -m pip install -r requirements.txt
python scripts/run_all.py --chapter 34
```

For Chapter 32A, `--chapter 32A` executes all three distinct Chapter 32A laboratories. You may also open the notebook and choose Restart & Run All. It writes a generated dataset CSV, JSON metrics and named PNG figure to repository-relative paths.

## Inputs and outputs
- Input: transparent seeded synthetic generation in `scripts/new_labs_engine.py`, code key `34`.
- Dataset: `datasets/generated/chapter_34__prediction_leakage_and_temporal_shift__synthetic.csv`
- Figure: `outputs/figures/chapter_34__prediction_leakage_and_temporal_shift.png`
- Metrics: `outputs/metrics/chapter_34__prediction_leakage_and_temporal_shift.json`
- Tested notebook: `outputs/executed_notebooks/chapter_34__prediction_leakage_and_temporal_shift.ipynb`

## Interpretation, validation, and limits
The validation cell checks execution artifacts and the number of generated observations. Examine method-specific numeric metrics and analytical assumptions before drawing scientific conclusions. Execution of synthetic examples is not a substitute for expert methodological review.
