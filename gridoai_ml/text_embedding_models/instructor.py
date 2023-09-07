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

    def calc(
        self, texts: t.List[str], instruction: t.Optional[str] = None
    ) -> t.List[t.List[float]]:
        embeddings = self.model.encode(
            [[instruction or self.instruction, text] for text in texts]
        )
        vecs = embeddings[0]
        return [vec.tolist() for vec in vecs]
