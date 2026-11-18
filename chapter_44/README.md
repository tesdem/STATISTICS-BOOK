# Chapter 44 — The Future of Statistical Science: New Data, New Methods and Enduring Principles

Notebook: `chapter_44__statistical_monitoring_under_distribution_shift.ipynb`

## WHAT
This laboratory explores **statistical monitoring under distribution shift**, focusing on: Technological change expands statistical reach but does not abolish questions of representativeness, assumptions, reproducibility, and consequence. Future practice should be judged by whether it improves reproducibility, calibration, transparency, and consequential decision quality.

## WHY
It provides a controlled teaching example of the chapter's main evidential distinction. The data are **realistic but synthetic**; no uploaded observational dataset or external source is used in this specific lab.

## HOW
From the repository root, run:

```bash
python -m pip install -r requirements.txt
python scripts/run_all.py --chapter 44
```

For Chapter 32A, `--chapter 32A` executes all three distinct Chapter 32A laboratories. You may also open the notebook and choose Restart & Run All. It writes a generated dataset CSV, JSON metrics and named PNG figure to repository-relative paths.

## Inputs and outputs
- Input: transparent seeded synthetic generation in `scripts/new_labs_engine.py`, code key `44`.
- Dataset: `datasets/generated/chapter_44__statistical_monitoring_under_distribution_shift__synthetic.csv`
- Figure: `outputs/figures/chapter_44__statistical_monitoring_under_distribution_shift.png`
- Metrics: `outputs/metrics/chapter_44__statistical_monitoring_under_distribution_shift.json`
- Tested notebook: `outputs/executed_notebooks/chapter_44__statistical_monitoring_under_distribution_shift.ipynb`

## Interpretation, validation, and limits
The validation cell checks execution artifacts and the number of generated observations. Examine method-specific numeric metrics and analytical assumptions before drawing scientific conclusions. Execution of synthetic examples is not a substitute for expert methodological review.
