# Week 1 — Exercise 1: Individual Metadata Creation

Individual exercise for the Data Management course: create DataCite (XML) and schema.org (JSON-LD) metadata for a publicly available dataset.

## Author

- Mirang Bhandari (individual submission)

## Dataset

**OnlyTrivial_dt** — the *class-level trivial refactorings* split of the **ML4Refactoring** dataset by Aniche et al.

- Landing page / DOI: <https://doi.org/10.5281/zenodo.3547639>
- Publisher: Zenodo
- License: CC-BY-4.0
- Format: CSV (232,468 rows × 53 columns, ~49 MB)
- Related publication: Aniche, M., Maziero, E., Durelli, R., Durelli, V. H. S. (2020). *The Effectiveness of Supervised Machine Learning Algorithms in Predicting Software Refactoring.* IEEE TSE. DOI: [10.1109/TSE.2020.3021736](https://doi.org/10.1109/TSE.2020.3021736)

Each row is one Java class snapshot carrying CK software metrics (CBO, WMC, DIT, NOC, RFC, LCOM, LCOM*, TCC, LCC, method/field counts, LOC, AST counters) plus a binary `refactoring` label marking whether a trivial class-level refactoring was applied at that commit.

## Repository layout

```
Week_1_Exercise_1_Individual_Metadata_Creation/
├── Dataset/
│   └── OnlyTrivial_dt (1).csv          # source dataset
├── Week_1_Exercise_1_Individual_Metadata_Creation.ipynb  # metadata builder
├── onlytrivial_datacite.xml            # DataCite 4.5 metadata
├── onlytrivial_schemaorg.json          # schema.org JSON-LD (@type: Dataset)
├── pyproject.toml                      # uv-managed project spec
└── README.md
```

## How to reproduce

The project uses [uv](https://docs.astral.sh/uv/) and a local `.venv`.

```bash
# from this directory
uv sync                                         # install pandas, lxml, jupyter
source .venv/Scripts/activate                   # Windows (Git Bash)
jupyter nbconvert --to notebook --execute --inplace \
  Week_1_Exercise_1_Individual_Metadata_Creation.ipynb
```

Re-executing the notebook regenerates `onlytrivial_datacite.xml` and `onlytrivial_schemaorg.json` from the CSV.

## Metadata standards applied

- **DataCite Metadata Schema 4.5** (`http://datacite.org/schema/kernel-4`) — required properties (Identifier, Creator, Title, Publisher, PublicationYear, ResourceType) plus Subjects, Language, Sizes, Formats, Version, Rights, Description (Abstract), and RelatedIdentifier for the companion publication.
- **schema.org Dataset** (`https://schema.org/Dataset`) — `@type: Dataset` with identifier, creator (with ORCID where available), publisher, license, distribution (DataDownload with SHA-256), keywords, and a `variableMeasured` array enumerating every CSV column.
