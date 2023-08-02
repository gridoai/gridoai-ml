from gridoai_ml.text_embedding_models.abs_model import AbsTextEmbeddingModel
from sentence_transformers import SentenceTransformer
import typing as t
import numpy as np


class MultilingualE5BaseModel(AbsTextEmbeddingModel):
    def __init__(self) -> None:
        self.model = SentenceTransformer("intfloat/multilingual-e5-base")
        self.instruction = "Represent the document:"

    @property
    def dim(self) -> int:
        return 768

    def calc(
        self, text: str, instruction: t.Optional[str] = None
    ) -> t.Optional[np.ndarray]:
        current_instruction = instruction or self.instruction
        embeddings = self.model.encode([f"{current_instruction}: {text}"])
        return embeddings[0]
