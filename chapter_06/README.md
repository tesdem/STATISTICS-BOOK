# Chapter 06 — Political Arithmetic and the Birth of Modern Statistics

Notebook: `chapter_06__mortality_counts_and_population_denominators.ipynb`

## WHAT
This laboratory explores **mortality counts and population denominators**, focusing on: The systematic use of numerical records to argue about society marks a turning point in the history of evidence.

## WHY
It provides a controlled teaching example of the chapter's main evidential distinction. The data are **realistic but synthetic**; no uploaded observational dataset or external source is used in this specific lab.

## HOW
From the repository root, run:

```bash
python -m pip install -r requirements.txt
python scripts/run_all.py --chapter 06
```

For Chapter 32A, `--chapter 32A` executes all three distinct Chapter 32A laboratories. You may also open the notebook and choose Restart & Run All. It writes a generated dataset CSV, JSON metrics and named PNG figure to repository-relative paths.

## Inputs and outputs
- Input: transparent seeded synthetic generation in `scripts/new_labs_engine.py`, code key `06`.
- Dataset: `datasets/generated/chapter_06__mortality_counts_and_population_denominators__synthetic.csv`
- Figure: `outputs/figures/chapter_06__mortality_counts_and_population_denominators.png`
- Metrics: `outputs/metrics/chapter_06__mortality_counts_and_population_denominators.json`
- Tested notebook: `outputs/executed_notebooks/chapter_06__mortality_counts_and_population_denominators.ipynb`

## Interpretation, validation, and limits
The validation cell checks execution artifacts and the number of generated observations. Examine method-specific numeric metrics and analytical assumptions before drawing scientific conclusions. Execution of synthetic examples is not a substitute for expert methodological review.
