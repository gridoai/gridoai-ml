import typing as t
import numpy as np
from context_handler.models import word2vec

def calc(text: str) -> t.Optional[np.ndarray]:
    """
    Calculate related vector for each word using word2vec and take the average.
    """
    maybe_vecs = [word2vec.calc(word) for word in text.split()]
    vecs = [vec for vec in maybe_vecs if vec is not None]
    return None if len(vecs) == 0 else np.mean(vecs)