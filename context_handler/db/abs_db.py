from abc import ABCMeta, abstractmethod
import typing as t
from uuid import UUID


class AbsDatabase(metaclass=ABCMeta):
    @abstractmethod
    def write_vec(self, uid: UUID, vec: t.List[float]) -> None:
        pass

    @abstractmethod
    def get_near_vecs(self, vec: t.List[float], k: int) -> t.List[t.Tuple[UUID, float]]:
        pass

    @abstractmethod
    def delete_doc(self, uid: UUID) -> None:
        pass
