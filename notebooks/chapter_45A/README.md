# Chapter 45A — Artificial Intelligence and the Transformation of Statistical Systems

**Companion computational laboratory:** From model performance to statistical product validity

Companion to *Statistics: The Science of Evidence, Uncertainty and Decision-Making*, Chapter 45A, Part XII.

## 1. Purpose and scientific rationale

The scientific credibility of a statistical deliverable depends on the entire production system, not merely the predictive accuracy of its constituent models. This laboratory investigates how measurement perturbations, missingness, classification errors, estimation procedures and release controls affect a final statistical indicator. It compares conventional, AI-assisted and bounded agentic workflows without assuming that greater technological complexity produces better evidence.

## 2. Files and repository

- `Chapter_45A_Laboratory.ipynb` — standalone executable notebook, including saved results and a bias boxplot.
- `README.md` — this guide.

Suggested location: `chapter_45a/` in [STATISTICS-BOOK](https://github.com/tesdem/STATISTICS-BOOK). The location is proposed, not a confirmation of upload.

## 3. Dataset and experimental design

The notebook uses the Wisconsin Diagnostic Breast Cancer dataset bundled with scikit-learn (569 observations, 30 numerical features). No separate download or external AI service is required.

- [scikit-learn dataset documentation](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html)
- [UCI original dataset and attribution](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic)

The target is the malignant-label fraction in a fixed held-out reference set of 171 observations (64 malignant labels; 37.43%). This is a finite teaching reference set, not a representative clinical population.

Stratified splits separate training, calibration and reference observations. The experiment draws 150 samples of 100 observations with replacement from the reference set. Each repetition applies a shared normally distributed perturbation to radius and perimeter features (standard deviation 0.6 for radius and five times the same shock for perimeter), representing correlated production measurement errors, and independently introduces 3% cell-level missingness. Calibration data are also corrupted. The three workflows share the same sample and corrupted calibration inputs. Each workflow uses 100 bootstrap draws per repetition to construct percentile intervals, with separate sample and calibration resampling.

## 4. Production architectures

| System | Architecture | Implementation |
|---|---|---|
| A | Conventional | Training-median radius threshold, missing radius replaced by threshold, uncorrected classified prevalence. |
| B | AI-assisted | Mean imputation, standardisation and logistic regression; prevalence correction using calibration sensitivity and specificity. |
| C | Bounded agentic | System B classifier with deterministic review flags for missing features or probabilities near 0.5, radius-based fallback for uncertain predictions with observed radius, and calibration-based prevalence correction. |

System C is a deterministic orchestration demonstration, not a deployed autonomous agent or LLM. Review flags are not measured human labour. Production labels are not used to make production decisions; they are used retrospectively for evaluation. Training and calibration labels are used for model fitting and calibration respectively.

## 5. Statistical framework

For classified prevalence `q`, sensitivity `Se` and specificity `Sp`, the corrected prevalence is:

```text
p_hat = (q + Sp - 1) / (Se + Sp - 1)
```

The notebook uses smoothed calibration rates and rejects correction when the denominator is at most 0.15. Estimates are not silently clipped. The numerical release gate requires a finite estimate in [0,1], a valid interval, maximum calibration subgroup error no greater than 35%, and interval width no greater than 0.45. These are illustrative thresholds, not official publication standards.

## 6. Evaluation metrics

- Bias: mean estimate minus finite reference prevalence.
- MSE: mean squared deviation from reference prevalence.
- Coverage: proportion of intervals containing reference prevalence; invalid intervals count as failures.
- Valid intervals: proportion meeting the notebook's finite-bootstrap criterion (at least 95 finite draws).
- Subgroup error: classification error below/above a fixed training-derived radius threshold, using uncorrupted reference features for retrospective grouping.
- Review burden: flags per 100 sampled records.
- Latency: elapsed computation time including bootstrap evaluation; hardware dependent.
- Blocked releases: number failing the numerical gate.
- Reproducibility: seeded random generation and structural assertions for 450 workflow records (150 repetitions × 3 systems).

Bias and MSE exclude nonfinite estimates through pandas aggregation; inspect interval validity and release rates alongside them.

## 7. Saved experimental results

The following values are from the notebook's saved execution, rounded as displayed.

| Metric | A | B | C |
|---|---:|---:|---:|
| Mean bias (percentage points) | +13.29 | +0.47 | −1.29 |
| MSE (proportion squared) | 0.0202 | 0.0024 | 0.0027 |
| Empirical interval coverage (%) | 24.67 | 94.00 | 93.33 |
| Review flags per 100 records | 0 | 0 | 61.75 |
| Mean latency (ms, saved run) | 42.1 | 43.4 | 43.2 |
| Release rate (%) | 46 | 100 | 100 |
| Blocked releases (of 150) | 81 | 0 | 0 |

System B has the lowest MSE in this experiment, approximately 88% lower than A. B and C approach the nominal 95% interval coverage, whereas A substantially undercovers. C incurs additional review flags without improving MSE over B. Differences reflect combined classification and estimation choices; they do not isolate the causal effect of orchestration. Numerical gate passage does not establish scientific validity or authorise official publication.

The manuscript figure may report timings from another execution; latency is not expected to reproduce exactly. The notebook itself prints a summary table and displays a bias boxplot; the manuscript's eight-panel figure is a separate presentation of laboratory results.

## 8. Installation and execution

Use Python 3 and a virtual environment. The saved notebook metadata identifies Python 3.13.5; exact dependency versions were not recorded in the notebook.

```bash
python -m venv .venv
```

Activate on macOS/Linux:

```bash
source .venv/bin/activate
```

Activate on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies and launch:

```bash
python -m pip install numpy pandas scipy scikit-learn matplotlib notebook
jupyter notebook Chapter_45A_Laboratory.ipynb
```

Select the Python kernel associated with the environment, restart the kernel and run all cells in order. Inspect the reference target, summary table, conditional released bias, boxplot and structural assertions. No API key, cloud service or GPU is required.

Optional headless execution (install `nbconvert` if necessary):

```bash
python -m pip install nbconvert
jupyter nbconvert --to notebook --execute Chapter_45A_Laboratory.ipynb --output Chapter_45A_Executed.ipynb
```

## 9. Reproducibility and limitations

The notebook uses NumPy seed 45 and split seeds 45 and 46. Saved outputs demonstrate execution and the structural assertions passed. Independent clean-environment reproduction and exact dependency pinning remain outstanding. Runtime varies by hardware and software. Bootstrap coverage is empirical for this particular simulation, not a general guarantee. Bootstrap draws are generated sequentially for each workflow, rather than sharing identical resampling indices across systems.

The observational dataset is real; the production defects and workflows are simulated. No clinical prevalence, causal effects, institutional deployment performance, actual human review workload or real publication authority can be inferred. Confidentiality and security controls are not implemented by the numerical gate.

## 10. Suggested extensions

- Apply identical prevalence correction to all three classifiers to separate estimation choices from classification choices.
- Vary corruption intensity, missingness mechanism, calibration size and subgroup definitions.
- Investigate sensitivity to release thresholds and fallback rules.
- Increase bootstrap repetitions and assess Monte Carlo variability.
- Record exact package versions and independently reproduce the experiment in a clean environment.
- Compare paired workflow differences and evaluate uncertainty in those differences.

## 11. Citation and responsible use

When using this laboratory, cite Chapter 45A of *Statistics: The Science of Evidence, Uncertainty and Decision-Making*, the notebook and the original dataset source linked above. Follow the repository's applicable licensing terms and the dataset's attribution requirements. This laboratory is intended for statistical education and methodological investigation, not clinical decision-making.
