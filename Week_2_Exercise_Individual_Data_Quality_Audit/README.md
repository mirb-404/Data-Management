# Week 2 — Exercise: Mini Data Quality Audit

Individual exercise for the Data Management course: perform a structured data quality audit on a messy customer transactions dataset, map issues to quality dimensions, compute KPIs, define validation rules, and recommend cleaning steps.

## Author

- Mirang Bhandari (individual submission)

## Dataset

**week2_customer_transactions_messy.csv** — a synthetic sample of 11 customer payment transactions intentionally seeded with data quality issues.

- Format: CSV (11 rows × 9 columns)
- Source: course-provided dataset (Data Management, Week 2)

Each row is one financial transaction carrying: a transaction ID, customer ID, transaction date, amount, currency, payment method, status (completed / pending / cancelled), region, and a last-updated timestamp. The dataset contains deliberate issues across all five quality dimensions used in the audit.

## Repository layout

```
Week_2_Exercise_Individual_Data_Quality_Audit/
├── new.ipynb                                        # completed audit notebook
├── 05_individual_exercise_data_quality_audit.ipynb  # original exercise template
├── week2_customer_transactions_messy.csv            # dataset
└── README.md
```

## How to reproduce

The project uses the shared virtual environment at the repository root.

```bash
# from the repo root
.venv\Scripts\activate.bat

# then open the notebook
jupyter notebook Week_2_Exercise_Individual_Data_Quality_Audit/new.ipynb
```

Run all cells top to bottom (`Kernel → Restart & Run All`). All outputs are reproducible from the CSV with no external dependencies.

## What the notebook covers

- **Task 1 – Dataset description:** brief overview of the schema and business context
- **Task 2 – Issues by dimension:** 13 issues mapped across Completeness, Uniqueness, Validity, Consistency, and Integrity
- **Task 3 – KPI summary:** four KPIs (Completeness Rate, Duplication Rate, Validity Error Rate, Format Consistency Score) with targets and pass/fail status
- **Task 4 – Validation rules:** five automatic rules that flag problematic records, with a per-record violation table
- **Task 5 – Audit summary:** issue type, affected row count, severity, and recommended next action for every identified issue
- **Task 6 – Cleaning recommendations:** six targeted steps for the next chapter (de-duplication, date normalisation, negative-amount handling, missing-field recovery, categorical standardisation, outlier review)
- **Bonus:** reusable `run_validation_rules()` helper function
