# STATISTICS-BOOK — Full Companion Laboratory Repository

**Intended destination:** https://github.com/tesdem/STATISTICS-BOOK  
**Book:** *Statistics: The Science of Evidence, Uncertainty and Decision-Making*  
**Scope:** 48 original chapters + Chapter 32A; 51 notebooks total (three Chapter 32A laboratories).

## Purpose (WHAT, WHY and HOW)

**WHAT:** Each chapter has a notebook illustrating a statistical principle and producing reproducible numerical metrics and an intuitively named PNG figure. All newly added chapters generate their own synthetic dataset; the original 27 revised chapters retain their supplied synthetic demonstrations.

**WHY:** The computational work makes assumptions, estimands, method limitations, sampling variability, leakage, fairness trade-offs and decision consequences visible. It is teaching evidence, **not** independent empirical or mathematical scientific certification.

**HOW:** Create a Python environment, install pinned dependencies, run `scripts/run_complete_book.py`, inspect the `reports/` logs, review the Chapter Index, and open the generated figure/metric files. Chapter-specific READMEs document the motivation and method.

## Full chapter index

See [docs/CHAPTER_INDEX.md](docs/CHAPTER_INDEX.md) for **all 51** notebooks, their exact titles and paths, and [docs/new_notebooks_manifest.json](docs/new_notebooks_manifest.json) for the newly created labs.

## Installation — macOS/Linux

```bash
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip check
python scripts/run_complete_book.py
python scripts/verify_complete_book.py
```

## Installation — Windows PowerShell

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip check
python scripts/run_complete_book.py
python scripts/verify_complete_book.py
```

The current audit uses the installed runtime. A completely independent environment rebuilt from network-fetched packages is **not** claimed. If package installation is unavailable, create an offline wheelhouse or supply a verified package mirror.

## Reproduce a chapter

```bash
python scripts/run_complete_book.py --chapter 21
python scripts/run_complete_book.py --chapter 32A
```

Alternatively launch Jupyter from the repository root and run all cells in the selected notebook. New notebooks import the transparent generator in `scripts/new_labs_engine.py`; keep that relative file in the cloned repository.

## Repository structure

```text
notebooks/chapter_01/ ... chapter_48/     one README per chapter
notebooks/chapter_32a/                    three Chapter 32A laboratories
datasets/generated/                       chapter-prefixed simulated CSV datasets
datasets/raw_archives/                    supplied external sources — licences require review
datasets/extracted/                       extracted observational source files
datasets/DATASET_CATALOG.md              evidence and licence caveats
outputs/figures/                          intuitively named chapter-numbered PNGs
outputs/metrics/                          JSON numeric outputs
outputs/executed_notebooks/               executed Jupyter notebooks
scripts/new_labs_engine.py                transparent new simulations
scripts/run_complete_book.py              full Jupyter-kernel batch runner
scripts/verify_complete_book.py           output and scientific sanity checks
reports/complete_execution_report.csv     status, durations, retry counts
docs/CHAPTER_INDEX.md                     chapter-to-file index
```

## Chapter 32A scope

- `chapter_32a__decision_reversal_radius.ipynb`: epsilon-contamination decision reversal for a specified two-state loss difference.
- `chapter_32a_b__coupled_uncertainty_budget.ipynb`: multiple action comparisons under a **shared distributional** uncertainty budget, not a resource allocation budget.
- `chapter_32a_c__resource_constrained_policy_regret.ipynb`: fractional resource allocation using linear programming, plus the regret of retaining a baseline policy after gains change. This does not solve integer or general distributionally robust optimisation.

## Evidence and dataset boundaries

Synthetic datasets are clearly distinguished from user-supplied observed data. New synthetic data are built locally and saved as CSV by executing the notebooks. The uploaded public data archives were retained for optional extensions; their licences and redistribution permissions must be checked before public upload. Observational archives are **not** used to compute the reported synthetic laboratory results. Never claim causal identification, external validity, historical accuracy or deployment safety based only on these demonstrations.

## Figures and numerical evidence

For each notebook the figure filename starts with `chapter_XX__` (or `chapter_32a...`), followed by a descriptive scientific title. The corresponding JSON contains the seed, evidence classification, metrics and generated dataset path. Regenerated outputs are considered consistent under the tested conditions; repeatability does not independently certify correctness.

## Publishing to GitHub

1. Inspect [docs/CHAPTER_INDEX.md](docs/CHAPTER_INDEX.md), `reports/` and licences.
2. Use the **code-and-generated-data package** as the safest initial public repository upload; large unverified source archives are intentionally excluded from that ZIP.
3. After licence checks, add eligible source datasets by release or Git LFS if necessary.
4. Never commit `.venv/`, cache files, credentials or private records.

## External scientific review

The manuscript is an **external-review candidate**. Synthetic laboratory execution is not independent expert certification. Mathematical derivations, estimator assumptions, data provenance, licence terms and production claims still require independent review.
