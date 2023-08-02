from abc import ABCMeta, abstractmethod
import numpy as np
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
        self, text: str, instruction: t.Optional[str] = None
    ) -> t.Optional[np.ndarray]:
        pass
