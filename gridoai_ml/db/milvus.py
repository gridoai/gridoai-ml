import typing as t
from uuid import UUID
from pymilvus import connections
from gridoai_ml.db.abs_db import AbsDatabase
from gridoai_ml.entities import DatabaseCredentials
import typing as t
from pymilvus import CollectionSchema, FieldSchema, DataType, Collection


class MilvusDatabase(AbsDatabase):
    def __init__(
        self, database_credentials: DatabaseCredentials, model_dim: int
    ) -> None:
        connections.connect(
            alias="default",
            user=database_credentials.username,
            password=database_credentials.password,
            timeout=30,
            uri=database_credentials.uri,
        )
        schema = CollectionSchema(
            fields=[
                FieldSchema(
                    name="uid", dtype=DataType.VARCHAR, max_length=255, is_primary=True
                ),
                FieldSchema(name="vec", dtype=DataType.FLOAT_VECTOR, dim=model_dim),
            ],
            description="document vector space",
        )
        index_params = {
            "metric_type": "L2",
            "index_type": "AUTOINDEX",
            "params": {"nlist": 1024},
        }
        self.collection = Collection(name="documents", schema=schema)
        self.collection.release()
        self.collection.create_index(field_name="vec", index_params=index_params)
        self.collection.load()

    def write_vec(self, uid: UUID, vec: t.List[float]) -> None:
        self.collection.insert([[str(uid)], [vec]])

    def get_near_vecs(self, vec: t.List[float], k: int) -> t.List[t.Tuple[UUID, float]]:
        search_params = {"metric_type": "L2", "params": {"nprobe": 10}}
        results = self.collection.search(
            data=[vec],
            anns_field="vec",
            param=search_params,
            limit=k,
            output_fields=["uid"],
            consistency_level="Strong",
        )
        return [(UUID(str(result.id)), result.distance) for result in results[0]]

    def delete_doc(self, uid: UUID) -> None:
        self.collection.delete(f"uid in ['{str(uid)}']")
