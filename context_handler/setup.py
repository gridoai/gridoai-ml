from context_handler.utils import _raise
from context_handler.entities import DatabaseCredentials, SetupData
from dotenv import load_dotenv
import os
import typing as t

CODE_ENV = os.environ.get("CODE_ENV") or "LOCAL"
load_dotenv()

with open("/tmp/service-account-file.json") as f:
    s = f.read().strip()
    print(f" s: { s}")
    
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


USE_MOCKED_MODEL = get_env("USE_MOCKED_MODEL")
DATABASE_TYPE = get_env("DATABASE_TYPE")
DB_URI = get_env("DB_URI")
DB_USER = get_env("DB_USER")
DB_PASS = get_env("DB_PASS")

setup_data = SetupData(
    database_type=DATABASE_TYPE,
    use_mocked_model=USE_MOCKED_MODEL == "TRUE",
    database_credentials=DatabaseCredentials(
        uri=DB_URI,
        username=DB_USER,
        password=DB_PASS,
    ),
)

print(f"code_env: {CODE_ENV}")
print(f"database_type: {setup_data.database_type}")
print(f"use_mocked_model: {setup_data.use_mocked_model}")
