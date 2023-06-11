from gridoai_ml.db.abs_db import AbsDatabase
from gridoai_ml.db.milvus import MilvusDatabase
from gridoai_ml.entities import SetupData
import typing as t

DATABASES: t.Dict[str, t.Type[AbsDatabase]] = {"milvus": MilvusDatabase}


def get_database(setup_data: SetupData, model_dim: int) -> AbsDatabase:
    return DATABASES[setup_data.database_type](
        setup_data.database_credentials, model_dim
    )
