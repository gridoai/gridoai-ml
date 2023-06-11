from abc import ABCMeta, abstractmethod
import typing as t
from uuid import UUID
from gridoai_ml.entities import DatabaseCredentials


class AbsDatabase(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, credentials: DatabaseCredentials, model_dim: int):
        pass

    @abstractmethod
    def write_vec(self, uid: UUID, vec: t.List[float]) -> None:
        pass

    @abstractmethod
    def get_near_vecs(self, vec: t.List[float], k: int) -> t.List[t.Tuple[UUID, float]]:
        pass

    @abstractmethod
    def delete_doc(self, uid: UUID) -> None:
        pass
