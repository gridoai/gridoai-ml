from gridoai_ml.text_embedding_models.abs_model import AbsTextEmbeddingModel
# from gridoai_ml.text_embedding_models.doc2vec import Doc2Vec
from gridoai_ml.text_embedding_models.mocked import MockedModel
# from gridoai_ml.text_embedding_models.instructor import InstructorModel
from gridoai_ml.text_embedding_models.multilingual_e5_base import (
    MultilingualE5BaseModel,
)
from gridoai_ml.entities import SetupData
import typing as t

MODELS: t.Dict[str, t.Type[AbsTextEmbeddingModel]] = {
    "mocked": MockedModel,
    # "doc2vec": Doc2Vec,
    # "instructor": InstructorModel,
    "multilingual-e5-base": MultilingualE5BaseModel,
}


def get_model(setup_data: SetupData) -> AbsTextEmbeddingModel:
    return MODELS[setup_data.embedding_model]()
