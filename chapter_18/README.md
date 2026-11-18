# Chapter 18 — Variation, Randomness and Statistical Regularity

Notebook: `chapter_18__sampling_regularity_and_dependence.ipynb`

## WHAT
This laboratory explores **sampling regularity and dependence**, focusing on: Variation is the substance of statistical inquiry; collective regularity emerges only under conditions that must be investigated rather than assumed.

## WHY
It provides a controlled teaching example of the chapter's main evidential distinction. The data are **realistic but synthetic**; no uploaded observational dataset or external source is used in this specific lab.

## HOW
From the repository root, run:

```bash
python -m pip install -r requirements.txt
python scripts/run_all.py --chapter 18
```

For Chapter 32A, `--chapter 32A` executes all three distinct Chapter 32A laboratories. You may also open the notebook and choose Restart & Run All. It writes a generated dataset CSV, JSON metrics and named PNG figure to repository-relative paths.

## Inputs and outputs
- Input: transparent seeded synthetic generation in `scripts/new_labs_engine.py`, code key `18`.
- Dataset: `datasets/generated/chapter_18__sampling_regularity_and_dependence__synthetic.csv`
- Figure: `outputs/figures/chapter_18__sampling_regularity_and_dependence.png`
- Metrics: `outputs/metrics/chapter_18__sampling_regularity_and_dependence.json`
- Tested notebook: `outputs/executed_notebooks/chapter_18__sampling_regularity_and_dependence.ipynb`

## Interpretation, validation, and limits
The validation cell checks execution artifacts and the number of generated observations. Examine method-specific numeric metrics and analytical assumptions before drawing scientific conclusions. Execution of synthetic examples is not a substitute for expert methodological review.
