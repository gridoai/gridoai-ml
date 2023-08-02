from gridoai_ml.text_embedding_models.abs_model import AbsTextEmbeddingModel
from gensim.models.keyedvectors import KeyedVectors
from google.cloud import storage
import numpy as np
import typing as t
import json
import os


class Doc2Vec(AbsTextEmbeddingModel):
    def __init__(self) -> None:
        self.word2vec_model = Doc2Vec.load_word2vec_model()

    @property
    def dim(self) -> int:
        return 300

    @staticmethod
    def load_word2vec_model() -> t.Dict[str, np.ndarray]:
        filename = "word2vec-google-news-300.model"
        if filename in os.listdir():
            return KeyedVectors.load(filename)
        path = f"/tmp/{filename}"
        bucket = storage.Client().get_bucket("grido-ml-models")
        blob_model = bucket.blob(f"{filename}")
        blob_vectors = bucket.blob(f"{filename}.vectors.npy")
        blob_model.download_to_filename(path)
        blob_vectors.download_to_filename(f"{path}.vectors.npy")
        return KeyedVectors.load(path)

    def calc(
        self, texts: t.List[str], instruction: t.Optional[str] = None
    ) -> t.List[np.ndarray]:
        return [self.calc_one(text, instruction) for text in texts]

    def calc_one(self, text: str, instruction: t.Optional[str] = None) -> np.ndarray:
        """
        Calculate related vector for each word using word2vec and take the average.
        """
        maybe_vecs = [self.word2vec_model.get(word) for word in text.split()]
        vecs = [vec for vec in maybe_vecs if vec is not None]
        if len(vecs) == 0:
            raise Exception("Cannot calculate vec for any word")
        return np.mean(vecs, axis=0)
