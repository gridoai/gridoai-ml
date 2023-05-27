from gensim.models.keyedvectors import KeyedVectors
import json
import os
import typing as t
import numpy as np

USE_MOCKED_MODEL = os.environ.get("USE_MOCKED_MODEL", "FALSE") == "TRUE"
print(f"Using mocked model: {USE_MOCKED_MODEL}")


def load_model() -> t.Dict[str, np.ndarray]:
    return KeyedVectors.load("word2vec-google-news-300.model")


def load_mocked_model() -> t.Dict[str, np.ndarray]:
    mocked_model = json.load(open("mocked_word2vec.json", "r"))

    class MockedModel(dict):
        def __getitem__(self, item) -> np.ndarray:
            return np.array(mocked_model[item])

    return MockedModel()


MODEL = load_model() if not USE_MOCKED_MODEL else load_mocked_model()


def calc(word: str) -> t.Optional[np.ndarray]:
    try:
        return MODEL[word]
    except:
        return None
