from pathlib import Path
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Project Root
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# -----------------------------
# App Settings
# -----------------------------
APP_NAME = os.getenv("APP_NAME", "CodeGuard v3")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
DEBUG = os.getenv("DEBUG", "True") == "True"

# -----------------------------
# API Keys
# -----------------------------
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# -----------------------------
# Database
# -----------------------------
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///codeguard.db"
)

# -----------------------------
# Paths
# -----------------------------
UPLOAD_FOLDER = BASE_DIR / os.getenv("UPLOAD_FOLDER", "uploads")

REPORT_FOLDER = BASE_DIR / os.getenv("REPORT_FOLDER", "reports")

KNOWLEDGE_BASE = BASE_DIR / os.getenv(
    "KNOWLEDGE_BASE",
    "knowledge_base/pdfs"
)

CHROMA_DB = BASE_DIR / os.getenv(
    "CHROMA_DB",
    "vector_db"
)

# -----------------------------
# Allowed File Types
# -----------------------------
ALLOWED_EXTENSIONS = [".py", ".java"]

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB

# -----------------------------
# PostgreSQL
# -----------------------------
from urllib.parse import quote_plus

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "codeguard_v3")
DB_USER = os.getenv("DB_USER", "postgres")

DB_PASSWORD = quote_plus(
    os.getenv("DB_PASSWORD", "")
)

DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
