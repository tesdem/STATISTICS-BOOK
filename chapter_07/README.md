# Chapter 07 — Probability, Measurement and the Rise of Mathematical Statistics

Notebook: `chapter_07__least_squares_precision_and_systematic_bias.ipynb`

## WHAT
This laboratory explores **least squares precision and systematic bias**, focusing on: Mathematical statistics turned variation and uncertainty into analysable objects, but mathematical precision is not the same as empirical validity.

## WHY
It provides a controlled teaching example of the chapter's main evidential distinction. The data are **realistic but synthetic**; no uploaded observational dataset or external source is used in this specific lab.

## HOW
From the repository root, run:

```bash
python -m pip install -r requirements.txt
python scripts/run_all.py --chapter 07
```

For Chapter 32A, `--chapter 32A` executes all three distinct Chapter 32A laboratories. You may also open the notebook and choose Restart & Run All. It writes a generated dataset CSV, JSON metrics and named PNG figure to repository-relative paths.

## Inputs and outputs
- Input: transparent seeded synthetic generation in `scripts/new_labs_engine.py`, code key `07`.
- Dataset: `datasets/generated/chapter_07__least_squares_precision_and_systematic_bias__synthetic.csv`
- Figure: `outputs/figures/chapter_07__least_squares_precision_and_systematic_bias.png`
- Metrics: `outputs/metrics/chapter_07__least_squares_precision_and_systematic_bias.json`
- Tested notebook: `outputs/executed_notebooks/chapter_07__least_squares_precision_and_systematic_bias.ipynb`

## Interpretation, validation, and limits
The validation cell checks execution artifacts and the number of generated observations. Examine method-specific numeric metrics and analytical assumptions before drawing scientific conclusions. Execution of synthetic examples is not a substitute for expert methodological review.
