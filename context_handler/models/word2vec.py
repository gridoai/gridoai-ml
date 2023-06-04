from gensim.models.keyedvectors import KeyedVectors
import json
import typing as t
import numpy as np
from google.cloud import storage
import os

service_account_info = json.loads(os.environ['GCP_KEY'])

# Create the storage client with the service account info
storage_client = storage.Client.from_service_account_info(service_account_info)

class Word2Vec:
    def __init__(self, use_mocked_model: bool) -> None:
        self.model = (
            Word2Vec.load_model()
            if not use_mocked_model
            else Word2Vec.load_mocked_model()
        )

    @staticmethod
    def load_model() -> t.Dict[str, np.ndarray]:
        filename = "word2vec-google-news-300.model"
        if filename in os.listdir():
            return KeyedVectors.load(filename)
        path = f"/tmp/{filename}"
        bucket = storage_client.get_bucket("grido-ml-models")
        blob_model = bucket.blob(f"{filename}")
        blob_vectors = bucket.blob(f"{filename}.vectors.npy")
        blob_model.download_to_filename(path)
        blob_vectors.download_to_filename(f"{path}.vectors.npy")
        return KeyedVectors.load(path)

    @staticmethod
    def load_mocked_model() -> t.Dict[str, np.ndarray]:
        mocked_model = json.load(open("mocked_word2vec.json", "r"))

        class MockedModel(dict):
            def __getitem__(self, item) -> np.ndarray:
                return np.array(mocked_model[item])

        return MockedModel()

    def calc(self, word: str) -> t.Optional[np.ndarray]:
        try:
            return self.model[word]
        except:
            return None
