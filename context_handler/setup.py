from context_handler.utils import _raise
from context_handler.entities import DatabaseCredentials, SetupData
from dotenv import load_dotenv
import os

load_dotenv()

USE_MOCKED_MODEL = os.environ.get("USE_MOCKED_MODEL", "FALSE") == "TRUE"
DATABASE_TYPE = os.environ.get("DATABASE_TYPE") or _raise(
    "DATABASE_TYPE env var should be set"
)
DB_HOST = os.environ.get("DB_HOST") or _raise("DB_HOST env var should be set")
DB_PORT = os.environ.get("DB_PORT") or _raise("DB_PORT env var should be set")
DB_USER = os.environ.get("DB_USER") or _raise("DB_USER env var should be set")
DB_PASS = os.environ.get("DB_PASS") or _raise("DB_PASS env var should be set")

setup_data = SetupData(
    database_type=DATABASE_TYPE,
    use_mocked_model=USE_MOCKED_MODEL,
    database_credentials=DatabaseCredentials(
        host=DB_HOST, port=int(DB_PORT), username=DB_USER, password=DB_PASS
    ),
)
