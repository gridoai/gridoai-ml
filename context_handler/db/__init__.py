from context_handler.db.abs_db import AbsDatabase
from context_handler.db.milvus import MilvusDatabase
import typing as t
import os

DATABASE_NAME = os.environ.get("DATABASE_NAME") or "milvus"
DATABASES: t.Dict[str, t.Type[AbsDatabase]] = {"milvus": MilvusDatabase}
database = DATABASES[DATABASE_NAME]()
