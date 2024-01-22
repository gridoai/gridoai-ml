from gridoai_ml.text_embedding_models.abs_model import AbsTextEmbeddingModel
from sentence_transformers import SentenceTransformer
import typing as t
import torch


class MultilingualE5BaseModel(AbsTextEmbeddingModel):
    def __init__(self) -> None:
        device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Device: {device}")
        self.model = SentenceTransformer(
            "intfloat/multilingual-e5-base",
            device=device,
        )

    @property
    def dim(self) -> int:
        return 768

    def calc(
        self, texts: t.List[str], instruction: t.Optional[str] = None
    ) -> t.List[t.List[float]]:
        if instruction:
            texts = [f"{instruction}: {text}" for text in texts]
        embeddings = self.model.encode(texts, convert_to_numpy=False)
        return [vec.tolist() for vec in embeddings]
