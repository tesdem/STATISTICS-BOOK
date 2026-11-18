# Chapter 09 — Technological Revolutions and Statistical Adaptation

Notebook: `chapter_09__technological_data_shift_and_selection.ipynb`

## WHAT
This laboratory explores **technological data shift and selection**, focusing on: Technology changes the questions society asks and the data available to answer them, but the core statistical challenges persist.

## WHY
It provides a controlled teaching example of the chapter's main evidential distinction. The data are **realistic but synthetic**; no uploaded observational dataset or external source is used in this specific lab.

## HOW
From the repository root, run:

```bash
python -m pip install -r requirements.txt
python scripts/run_all.py --chapter 09
```

For Chapter 32A, `--chapter 32A` executes all three distinct Chapter 32A laboratories. You may also open the notebook and choose Restart & Run All. It writes a generated dataset CSV, JSON metrics and named PNG figure to repository-relative paths.

## Inputs and outputs
- Input: transparent seeded synthetic generation in `scripts/new_labs_engine.py`, code key `09`.
- Dataset: `datasets/generated/chapter_09__technological_data_shift_and_selection__synthetic.csv`
- Figure: `outputs/figures/chapter_09__technological_data_shift_and_selection.png`
- Metrics: `outputs/metrics/chapter_09__technological_data_shift_and_selection.json`
- Tested notebook: `outputs/executed_notebooks/chapter_09__technological_data_shift_and_selection.ipynb`

## Interpretation, validation, and limits
The validation cell checks execution artifacts and the number of generated observations. Examine method-specific numeric metrics and analytical assumptions before drawing scientific conclusions. Execution of synthetic examples is not a substitute for expert methodological review.
