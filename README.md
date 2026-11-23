# STATISTICS-BOOK — MASTER_V9 Companion Repository

**Book:** Statistics: The Science of Evidence, Uncertainty and Decision-Making (MASTER_V9).

**Destination:** https://github.com/tesdem/STATISTICS-BOOK

**Inventory:** 54 notebook files for 52 chapter units (48 numbered chapters plus 22A, 27A, 32A, and 42A). Chapter 32A has three alternatives.

## Important provenance note
The pre-existing 51 GitHub notebooks could not be downloaded into the workspace, so this ZIP contains **new educational reconstructions** of the first 53 laboratory slots, **not verbatim copies of the original notebooks**. The historic RAND Chapter 42A notebook is copied from the available completed case study. If your existing GitHub notebooks contain more detailed or differently verified methods, retain them and merge only the additional V9 material, rather than blindly overwriting them.

## What, why and how
Each chapter notebook has a WHAT/WHY/HOW introduction, executable Python demonstration, seeded experiment, figures, machine-readable metrics and exercises. Synthetic results demonstrate methods under given assumptions; they do not certify real-world validity.

## Quick start

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/run_all_notebooks.py
```

Use `python scripts/verify_package.py` to check the inventory and outputs. See `docs/CHAPTER_INDEX.md`. To run an individual notebook, open it in Jupyter and execute all cells in sequence.

**Note:** Chapter 42A uses genuine historical RAND outpatient-visit observations, and its monetary costing and stress scenarios are hypothetical. Verify dataset redistribution permissions before publishing the CSV.

## GitHub upload

This ZIP is a local upload-ready working tree; it is not itself a remote repository and does not change your existing GitHub files. Unzip it, review the content against the public repository, then commit and push from Git, or use GitHub's **Add file → Upload files** for small groups. Detailed steps are in `UPLOAD_TO_GITHUB.md`.

## Scientific boundaries
Successful local execution demonstrates computation only. Literature attribution, estimator assumptions, empirical reproducibility, and external scientific review are separate requirements.
