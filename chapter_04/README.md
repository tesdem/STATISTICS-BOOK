# Chapter 04 — Statistical Thinking, Human Intuition and Cognitive Bias

Notebook: `chapter_04__screening_base_rates_and_predictive_value.ipynb`

## WHAT
This laboratory explores **screening base rates and predictive value**, focusing on: Human intuition needs empirical checks, especially when probability and selection are involved.

## WHY
It provides a controlled teaching example of the chapter's main evidential distinction. The data are **realistic but synthetic**; no uploaded observational dataset or external source is used in this specific lab.

## HOW
From the repository root, run:

```bash
python -m pip install -r requirements.txt
python scripts/run_all.py --chapter 04
```

For Chapter 32A, `--chapter 32A` executes all three distinct Chapter 32A laboratories. You may also open the notebook and choose Restart & Run All. It writes a generated dataset CSV, JSON metrics and named PNG figure to repository-relative paths.

## Inputs and outputs
- Input: transparent seeded synthetic generation in `scripts/new_labs_engine.py`, code key `04`.
- Dataset: `datasets/generated/chapter_04__screening_base_rates_and_predictive_value__synthetic.csv`
- Figure: `outputs/figures/chapter_04__screening_base_rates_and_predictive_value.png`
- Metrics: `outputs/metrics/chapter_04__screening_base_rates_and_predictive_value.json`
- Tested notebook: `outputs/executed_notebooks/chapter_04__screening_base_rates_and_predictive_value.ipynb`

## Interpretation, validation, and limits
The validation cell checks execution artifacts and the number of generated observations. Examine method-specific numeric metrics and analytical assumptions before drawing scientific conclusions. Execution of synthetic examples is not a substitute for expert methodological review.
