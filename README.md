
# PipeKit

An automated data-processing pipeline built with Python, NumPy, SQL, and AWS.

PipeKit is designed to import CSV datasets, validate records, identify data quality issues, and generate useful reports.

## Current Features (v0.1.0)

- Read CSV files using Python's built-in `csv` module
- Convert CSV rows into dictionaries
- Display imported records
- Count the total number of records


## Tech Stack

- Python
- NumPy
- SQLite (planned)
- AWS S3 and Lambda (planned)


### Prerequisites

- Python 3.10 or newer

### Installation

Clone the repository:

```bash
git clone https://github.com/Ryan-Barcarse/PipeKit
cd datapipeline
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Run the CSV reader:

```bash
python pipeline.py
```


## Roadmap

- [x] v0.1.0 — Initial CSV reader
- [ ] v0.2.0 — SQL database integration
- [ ] v0.3.0 — Data validation and cleaning
- [ ] v0.4.0 — NumPy analysis
- [ ] v0.5.0 — AWS integration
- [ ] v1.0.0 — Testing and documentation

