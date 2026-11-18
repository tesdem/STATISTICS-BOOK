# Chapter 13 — The Nature, Origins and Quality of Data

Notebook: `chapter_13__measurement_missingness_and_data_quality.ipynb`

## WHAT
This laboratory explores **measurement missingness and data quality**, focusing on: Data are produced by processes, not found ready-made; understanding those processes is essential for interpreting what the data can support.

## WHY
It provides a controlled teaching example of the chapter's main evidential distinction. The data are **realistic but synthetic**; no uploaded observational dataset or external source is used in this specific lab.

## HOW
From the repository root, run:

```bash
python -m pip install -r requirements.txt
python scripts/run_all.py --chapter 13
```

For Chapter 32A, `--chapter 32A` executes all three distinct Chapter 32A laboratories. You may also open the notebook and choose Restart & Run All. It writes a generated dataset CSV, JSON metrics and named PNG figure to repository-relative paths.

## Inputs and outputs
- Input: transparent seeded synthetic generation in `scripts/new_labs_engine.py`, code key `13`.
- Dataset: `datasets/generated/chapter_13__measurement_missingness_and_data_quality__synthetic.csv`
- Figure: `outputs/figures/chapter_13__measurement_missingness_and_data_quality.png`
- Metrics: `outputs/metrics/chapter_13__measurement_missingness_and_data_quality.json`
- Tested notebook: `outputs/executed_notebooks/chapter_13__measurement_missingness_and_data_quality.ipynb`

## Interpretation, validation, and limits
The validation cell checks execution artifacts and the number of generated observations. Examine method-specific numeric metrics and analytical assumptions before drawing scientific conclusions. Execution of synthetic examples is not a substitute for expert methodological review.
