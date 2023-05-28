from context_handler.db.abs_db import AbsDatabase
from context_handler.db.milvus import MilvusDatabase
from context_handler.entities import SetupData
import typing as t

DATABASES: t.Dict[str, t.Type[AbsDatabase]] = {"milvus": MilvusDatabase}


def get_database(setup_data: SetupData) -> AbsDatabase:
    return DATABASES[setup_data.database_type](setup_data.database_credentials)
