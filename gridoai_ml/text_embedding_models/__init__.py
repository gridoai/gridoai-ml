from gridoai_ml.text_embedding_models.abs_model import AbsTextEmbeddingModel
from gridoai_ml.entities import SetupData

def get_model(setup_data: SetupData) -> AbsTextEmbeddingModel:
    match setup_data.embedding_model:
        case "mocked":
            from gridoai_ml.text_embedding_models.mocked import MockedModel
            return MockedModel()
        case "multilingual-e5-base":
            from gridoai_ml.text_embedding_models.multilingual_e5_base import MultilingualE5BaseModel
            return MultilingualE5BaseModel()
        case "multilingual-e5-base-onnx":
            from gridoai_ml.text_embedding_models.multilingual_e5_base_onnx import OnnxRuntimeTextEmbeddingModel
            return OnnxRuntimeTextEmbeddingModel()
        case "doc2vec":
            from gridoai_ml.text_embedding_models.doc2vec import Doc2Vec
            return Doc2Vec()
        case "instructor":
            from gridoai_ml.text_embedding_models.instructor import InstructorModel
            return InstructorModel()

