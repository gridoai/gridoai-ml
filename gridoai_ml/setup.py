from gridoai_ml.utils import _raise
from gridoai_ml.entities import DatabaseCredentials, SetupData
from dotenv import load_dotenv
import os
import typing as t

CODE_ENV = os.environ.get("CODE_ENV") or "LOCAL"
load_dotenv()


def get_env(var: str) -> str:
    if CODE_ENV == "LOCAL":
        return os.environ.get(var) or _raise(f"{var} env var should be set")
    elif CODE_ENV == "DEV":
        return os.environ.get(f"DEV_{var}") or _raise(f"{var} env var should be set")
    else:
        return os.environ.get(f"PRD_{var}") or _raise(f"{var} env var should be set")


def get_optional_env(var: str) -> t.Optional[str]:
    if CODE_ENV == "LOCAL":
        return os.environ.get(var)
    elif CODE_ENV == "DEV":
        return os.environ.get(f"DEV_{var}")
    else:
        return os.environ.get(f"PRD_{var}")


EMBEDDING_MODEL = get_env("EMBEDDING_MODEL")
DATABASE_TYPE = get_optional_env("DATABASE_TYPE")
DB_URI = get_optional_env("DB_URI")
DB_USER = get_optional_env("DB_USER")
DB_PASS = get_optional_env("DB_PASS")

setup_data = SetupData(
    database_type=DATABASE_TYPE,
    embedding_model=EMBEDDING_MODEL,
    database_credentials=None
    if (DB_URI is None or DB_USER is None or DB_PASS is None or DATABASE_TYPE is None)
    else DatabaseCredentials(
        uri=DB_URI,
        username=DB_USER,
        password=DB_PASS,
    ),
)

print(f"code_env: {CODE_ENV}")
print(f"database_type: {setup_data.database_type}")
print(f"embedding_model: {setup_data.embedding_model}")
