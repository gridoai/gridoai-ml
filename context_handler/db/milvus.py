import typing as t
from uuid import UUID
from pymilvus import connections
from context_handler.db.abs_db import AbsDatabase
from context_handler.entities import DatabaseCredentials
import typing as t
from pymilvus import CollectionSchema, FieldSchema, DataType, Collection


class MilvusDatabase(AbsDatabase):
    def __init__(self, database_credentials: DatabaseCredentials) -> None:
        connections.connect(
            alias="default",
            user=database_credentials.username,
            password=database_credentials.password,
            host=database_credentials.host,
            port=database_credentials.port,
        )
        schema = CollectionSchema(
            fields=[
                FieldSchema(
                    name="uid", dtype=DataType.VARCHAR, max_length=255, is_primary=True
                ),
                FieldSchema(name="vec", dtype=DataType.FLOAT_VECTOR, dim=300),
            ],
            description="document vector space",
        )
        index_params = {
            "metric_type": "L2",
            "index_type": "IVF_FLAT",
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
