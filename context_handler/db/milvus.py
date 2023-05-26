import typing as t
from uuid import UUID
from pymilvus import connections
from context_handler.db.abs_db import AbsDatabase
import typing as t
from pymilvus import CollectionSchema, FieldSchema, DataType, Collection


class MilvusDatabase(AbsDatabase):
    def __init__(self) -> None:
        connections.connect(
            alias="default",
            user="username",
            password="password",
            host="localhost",
            port="19530",
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
        self.collection.create_index(field_name="vec", index_params=index_params)

    def write_vec(self, uid: UUID, vec: t.List[float]) -> None:
        self.collection.insert([{"uid": str(uid), "vec": vec}])

    def get_near_vecs(self, vec: t.List[float], k: int) -> t.List[t.Tuple[UUID, float]]:
        self.collection.load()
        search_params = {"metric_type": "L2", "params": {"nprobe": 10}}
        results = self.collection.search(
            data=vec,
            anns_field="vec",
            params=search_params,
            limit=k,
            output_fields=["uid"],
            consistency_level="Strong",
        )
        print(results)
        return [(UUID(str(result[0])), result[1]) for result in results]
