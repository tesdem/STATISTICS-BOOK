# Data provenance and licensing

All non-42A notebooks use deterministic synthetic data in the shared engine and do not require dataset download.

The Chapter 42A notebook uses `notebooks/chapter_42a/rand_hie_open_source_observations.csv`, a prepared 20,190-record extract of RAND Health Insurance Experiment utilisation data distributed with `statsmodels.datasets.randhie`. Refer to the original RAND experiment documentation and statsmodels dataset metadata for citation and terms. Redistribution rights should be reconfirmed before making this copy publicly available.

The observed target is doctor visits, not insurance claim payment. Assumed unit costs, premiums, solvency and stress distributions are hypothetical.
