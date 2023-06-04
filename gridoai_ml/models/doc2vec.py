import typing as t
import numpy as np
from gridoai_ml.models.word2vec import Word2Vec


class Doc2Vec:
    def __init__(self, use_mocked_model: bool) -> None:
        self.word2vec = Word2Vec(use_mocked_model)

    def calc(self, text: str) -> t.Optional[np.ndarray]:
        """
        Calculate related vector for each word using word2vec and take the average.
        """
        maybe_vecs = [self.word2vec.calc(word) for word in text.split()]
        vecs = [vec for vec in maybe_vecs if vec is not None]
        if len(vecs) == 0:
            return None
        return np.mean(vecs, axis=0)
