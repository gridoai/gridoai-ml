from abc import ABCMeta, abstractmethod
import typing as t

class AbsTextEmbeddingModel(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @property
    @abstractmethod
    def dim(self) -> int:
        pass

    @abstractmethod
    def calc(
        self, texts: t.List[str], instruction: t.Optional[str] = None
    ) -> t.List[t.List[float]]:
        pass
