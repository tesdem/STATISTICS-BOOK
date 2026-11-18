# Chapter 35 — The Evolution and Types of Artificial Intelligence: From Rules to Autonomous Systems

Notebook: `chapter_35__rules_statistical_learning_and_concept_shift.ipynb`

## WHAT
This laboratory explores **rules statistical learning and concept shift**, focusing on: AI is a family of approaches, not a single algorithm or scale of intelligence. A coherent taxonomy separates historical approach, learning paradigm, model architecture, system design, and degree of autonomy.

## WHY
It provides a controlled teaching example of the chapter's main evidential distinction. The data are **realistic but synthetic**; no uploaded observational dataset or external source is used in this specific lab.

## HOW
From the repository root, run:

```bash
python -m pip install -r requirements.txt
python scripts/run_all.py --chapter 35
```

For Chapter 32A, `--chapter 32A` executes all three distinct Chapter 32A laboratories. You may also open the notebook and choose Restart & Run All. It writes a generated dataset CSV, JSON metrics and named PNG figure to repository-relative paths.

## Inputs and outputs
- Input: transparent seeded synthetic generation in `scripts/new_labs_engine.py`, code key `35`.
- Dataset: `datasets/generated/chapter_35__rules_statistical_learning_and_concept_shift__synthetic.csv`
- Figure: `outputs/figures/chapter_35__rules_statistical_learning_and_concept_shift.png`
- Metrics: `outputs/metrics/chapter_35__rules_statistical_learning_and_concept_shift.json`
- Tested notebook: `outputs/executed_notebooks/chapter_35__rules_statistical_learning_and_concept_shift.ipynb`

## Interpretation, validation, and limits
The validation cell checks execution artifacts and the number of generated observations. Examine method-specific numeric metrics and analytical assumptions before drawing scientific conclusions. Execution of synthetic examples is not a substitute for expert methodological review.
