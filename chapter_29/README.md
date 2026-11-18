# Chapter 29 — Statistical Models: Simplifying Reality Without Losing Scientific Meaning

Notebook: `chapter_29__model_complexity_training_vs_test_error.ipynb`

## WHAT
This laboratory explores **model complexity training vs test error**, focusing on: A model is a deliberately simplified account of how observations arise; it translates a scientific question into variables, assumptions, and estimable quantities. Its value depends on matching the question, design, assumptions, analysis, and interpretation.

## WHY
It provides a controlled teaching example of the chapter's main evidential distinction. The data are **realistic but synthetic**; no uploaded observational dataset or external source is used in this specific lab.

## HOW
From the repository root, run:

```bash
python -m pip install -r requirements.txt
python scripts/run_all.py --chapter 29
```

For Chapter 32A, `--chapter 32A` executes all three distinct Chapter 32A laboratories. You may also open the notebook and choose Restart & Run All. It writes a generated dataset CSV, JSON metrics and named PNG figure to repository-relative paths.

## Inputs and outputs
- Input: transparent seeded synthetic generation in `scripts/new_labs_engine.py`, code key `29`.
- Dataset: `datasets/generated/chapter_29__model_complexity_training_vs_test_error__synthetic.csv`
- Figure: `outputs/figures/chapter_29__model_complexity_training_vs_test_error.png`
- Metrics: `outputs/metrics/chapter_29__model_complexity_training_vs_test_error.json`
- Tested notebook: `outputs/executed_notebooks/chapter_29__model_complexity_training_vs_test_error.ipynb`

## Interpretation, validation, and limits
The validation cell checks execution artifacts and the number of generated observations. Examine method-specific numeric metrics and analytical assumptions before drawing scientific conclusions. Execution of synthetic examples is not a substitute for expert methodological review.
