import sqlite3
import pandas as pd
import numpy as np
import os
import logging
from pathlib import Path
from datetime import datetime

# ── Logging setup ──────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger('etl')

# ── File paths ─────────────────────────────────────────────────────────────────
# Changed DATA_DIR to /content to match your file structure
DATA_DIR = Path('/content')
DB_PATH       = DATA_DIR / 'PerfectPetClub.db'
CRM_PATH      = DATA_DIR / 'PerfectPetClub_CRM_report.csv'
LOG_PATH      = DATA_DIR / 'PerfectPetClub_server_log.csv'
SURVEY_PATH   = DATA_DIR / 'PerfectPetClub_survey.csv'
OUTPUT_PARQUET = DATA_DIR / 'churn_dataset.parquet'

# Reference date for recency calculations (last day with sales in the dataset)
REFERENCE_DATE = pd.Timestamp('2026-11-10')

logger.info('Configuration loaded. Reference date: %s', REFERENCE_DATE.date())
