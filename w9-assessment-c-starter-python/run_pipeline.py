"""
Task 3 - Data Pipeline Build (Python)

Reads    data/raw.csv
Writes   data/clean.csv  and  data/export.json
Run:     python run_pipeline.py        (Windows: py run_pipeline.py)

Rules: no AI tools for this task. Use the built-in csv and json modules,
or pandas if you used it in class (pip install pandas).
Commit as you go:  scaffold -> feature -> refactor  (see your Task 3 instructions).
"""
import csv
import json
import logging
from pathlib import Path

ROOT = Path(__file__).parent
RAW_PATH = ROOT / "data" / "raw.csv"
CLEAN_PATH = ROOT / "data" / "clean.csv"
JSON_PATH = ROOT / "data" / "export.json"

# Logging (Week 7 standard: timestamp | level | message).
# Use log.info / log.warning at the key steps: start, rows read, anomalies found, rows written, finish.
logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
log = logging.getLogger("pipeline")


def load_raw(path):
    """TODO 1 - Load: read raw.csv into a header row and data rows.
    If Python refuses to read the file, read the error message carefully:
    it tells you exactly which byte it could not understand."""


def fix_headers(header_row):
    """TODO 2 - Headers: give every column a clear snake_case name.
    Some header cells are blank. Look at the data to decide what they hold."""


def clean_row(row):
    """TODO 3 - Clean one row: trim text, make types consistent (numbers are numbers,
    dates are one format), and decide what to do with null-like values
    (remove the row, fill a value, or flag it). Write your decisions in the cleaning log."""


def write_outputs(rows):
    """TODO 4 - Export: write the cleaned rows to clean.csv and export.json.
    Your JSON must be valid. Numbers should be numbers, not strings."""


def main():
    log.info("Pipeline start")
    # TODO 5 - Wire the steps together, logging rows read, anomalies found, and rows written.


if __name__ == "__main__":
    main()
