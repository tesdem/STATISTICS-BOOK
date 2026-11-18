# Chapter 37 — Can Artificial Intelligence Produce Scientific Knowledge? Discovery, Validation and Epistemic Integrity

Notebook: `chapter_37__multiple_testing_false_discoveries_and_replication.ipynb`

## WHAT
This laboratory explores **multiple testing false discoveries and replication**, focusing on: AI can accelerate discovery, but evidence becomes knowledge through clear assumptions, independent validation, causal scrutiny where needed, replication, and accountable interpretation.

## WHY
It provides a controlled teaching example of the chapter's main evidential distinction. The data are **realistic but synthetic**; no uploaded observational dataset or external source is used in this specific lab.

## HOW
From the repository root, run:

```bash
python -m pip install -r requirements.txt
python scripts/run_all.py --chapter 37
```

For Chapter 32A, `--chapter 32A` executes all three distinct Chapter 32A laboratories. You may also open the notebook and choose Restart & Run All. It writes a generated dataset CSV, JSON metrics and named PNG figure to repository-relative paths.

## Inputs and outputs
- Input: transparent seeded synthetic generation in `scripts/new_labs_engine.py`, code key `37`.
- Dataset: `datasets/generated/chapter_37__multiple_testing_false_discoveries_and_replication__synthetic.csv`
- Figure: `outputs/figures/chapter_37__multiple_testing_false_discoveries_and_replication.png`
- Metrics: `outputs/metrics/chapter_37__multiple_testing_false_discoveries_and_replication.json`
- Tested notebook: `outputs/executed_notebooks/chapter_37__multiple_testing_false_discoveries_and_replication.ipynb`

## Interpretation, validation, and limits
The validation cell checks execution artifacts and the number of generated observations. Examine method-specific numeric metrics and analytical assumptions before drawing scientific conclusions. Execution of synthetic examples is not a substitute for expert methodological review.
