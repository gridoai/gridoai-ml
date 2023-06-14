from gridoai_ml.text_embedding_models.abs_model import AbsTextEmbeddingModel
from InstructorEmbedding import INSTRUCTOR
import typing as t
import numpy as np


class InstructorModel(AbsTextEmbeddingModel):
    def __init__(self) -> None:
        self.model = INSTRUCTOR("hkunlp/instructor-large")
        self.instruction = "Represent the document:"

    @property
    def dim(self) -> int:
        return 768

    def calc(self, text: str) -> t.Optional[np.ndarray]:
        embeddings = self.model.encode([[self.instruction, text]])
        return embeddings[0]
