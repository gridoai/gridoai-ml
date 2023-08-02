from gridoai_ml.text_embedding_models.abs_model import AbsTextEmbeddingModel
import numpy as np
import typing as t
import json


class MockedModel(AbsTextEmbeddingModel):
    def __init__(self) -> None:
        self.mocked_model = json.load(open("mocked.json", "r"))

    @property
    def dim(self) -> int:
        return 300

    def calc(
        self, text: str, instruction: t.Optional[str] = None
    ) -> t.Optional[np.ndarray]:
        try:
            return np.array(self.mocked_model[text])
        except:
            return None
