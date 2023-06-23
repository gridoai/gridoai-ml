from gridoai_ml.db.abs_db import AbsDatabase
from gridoai_ml.db.milvus import MilvusDatabase
from gridoai_ml.entities import SetupData
import typing as t

DATABASES: t.Dict[str, t.Type[AbsDatabase]] = {"milvus": MilvusDatabase}


def get_database(setup_data: SetupData, model_dim: int) -> t.Optional[AbsDatabase]:
    return (
        None
        if setup_data.database_type is None or setup_data.database_credentials is None
        else DATABASES[setup_data.database_type](
            setup_data.database_credentials, model_dim
        )
    )
