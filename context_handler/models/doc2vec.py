import typing as t
import numpy as np
from context_handler.models import word2vec


def calc(text: str) -> t.Optional[np.ndarray[t.Any, np.dtype[np.floating]]]:
    """
    Calculate related vector for each word using word2vec and take the average.
    """
    maybe_vecs = [word2vec.calc(word) for word in text.split()]
    vecs = [vec for vec in maybe_vecs if vec is not None]
    if len(vecs) == 0:
        return None
    return np.mean(vecs, axis=0)
