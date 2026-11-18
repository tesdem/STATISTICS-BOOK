# Chapter 21 — Information Theory: Entropy, Divergence and the Limits of Quantification

Notebook: `chapter_21__information_entropy_and_permutation_testing.ipynb`

## WHAT
This laboratory explores **information entropy and permutation testing**, focusing on: Information theory provides rigorous measures of uncertainty and predictive association, yet meaning, validity, causality, and ethical worth require additional reasoning; quantifying information is not the same as establishing knowledge.

## WHY
It provides a controlled teaching example of the chapter's main evidential distinction. The data are **realistic but synthetic**; no uploaded observational dataset or external source is used in this specific lab.

## HOW
From the repository root, run:

```bash
python -m pip install -r requirements.txt
python scripts/run_all.py --chapter 21
```

For Chapter 32A, `--chapter 32A` executes all three distinct Chapter 32A laboratories. You may also open the notebook and choose Restart & Run All. It writes a generated dataset CSV, JSON metrics and named PNG figure to repository-relative paths.

## Inputs and outputs
- Input: transparent seeded synthetic generation in `scripts/new_labs_engine.py`, code key `21`.
- Dataset: `datasets/generated/chapter_21__information_entropy_and_permutation_testing__synthetic.csv`
- Figure: `outputs/figures/chapter_21__information_entropy_and_permutation_testing.png`
- Metrics: `outputs/metrics/chapter_21__information_entropy_and_permutation_testing.json`
- Tested notebook: `outputs/executed_notebooks/chapter_21__information_entropy_and_permutation_testing.ipynb`

## Interpretation, validation, and limits
The validation cell checks execution artifacts and the number of generated observations. Examine method-specific numeric metrics and analytical assumptions before drawing scientific conclusions. Execution of synthetic examples is not a substitute for expert methodological review.
