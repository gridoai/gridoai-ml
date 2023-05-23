from gensim.models.word2vec import Word2Vec
import json
import os
import typing as t
import numpy as np

USE_MOCKED_MODEL = os.environ.get("USE_MOCKED_MODEL", "FALSE") == "TRUE"
print(f"Using mocked model: {USE_MOCKED_MODEL}")
MODEL: t.Dict[str, np.ndarray] = Word2Vec.load("word2vec-google-news-300.model").wv if not USE_MOCKED_MODEL else json.load(open("mocked_word2vec.json", "r"))

def calc(word: str) -> t.Optional[np.ndarray]:
    try:
        return MODEL[word]
    except:
        return None