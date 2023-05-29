from context_handler.utils import _raise
from context_handler.entities import DatabaseCredentials, SetupData
from dotenv import load_dotenv
import os

CODE_ENV = os.environ.get("CODE_ENV") or "LOCAL"
load_dotenv()


def get_env(var: str) -> str:
    if CODE_ENV == "LOCAL":
        return os.environ.get(var) or _raise(f"{var} env var should be set")
    elif CODE_ENV == "DEV":
        return os.environ.get(f"DEV_{var}") or _raise(f"{var} env var should be set")
    else:
        return os.environ.get(f"PRD_{var}") or _raise(f"{var} env var should be set")


USE_MOCKED_MODEL = get_env("USE_MOCKED_MODEL")
DATABASE_TYPE = get_env("DATABASE_TYPE")
DB_HOST = get_env("DB_HOST")
DB_PORT = get_env("DB_PORT")
DB_USER = get_env("DB_USER")
DB_PASS = get_env("DB_PASS")

setup_data = SetupData(
    database_type=DATABASE_TYPE,
    use_mocked_model=USE_MOCKED_MODEL == "TRUE",
    database_credentials=DatabaseCredentials(
        host=DB_HOST, port=int(DB_PORT), username=DB_USER, password=DB_PASS
    ),
)

print(f"code_env: {CODE_ENV}")
print(f"database_type: {setup_data.database_type}")
print(f"use_mocked_model: {setup_data.use_mocked_model}")
