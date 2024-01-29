from modal import Stub, web_endpoint, Image, gpu
from gridoai_ml.setup import setup_data
from gridoai_ml.text_embedding_models import get_model
from gridoai_ml.entities import EmbeddingPayload


def download_model():
    get_model(setup_data)


image = (
    Image.debian_slim()
    .pip_install(
        "python-dotenv~=1.0.0",
        "requests~=2.31.0",
        "numpy",
        "sentence_transformers",
        "torch",
        "transformers",
        "huggingface-hub",
        "onnxruntime",
    )
    .env(
        {
            "SENTENCE_TRANSFORMERS_HOME": "./.cache/",
            "EMBEDDING_MODEL": "multilingual-e5-base",
        },
    )
    .run_function(download_model)
)

stub = Stub(
    name="gridoai-ml",
    image=image,
)


@stub.cls(
    gpu=gpu.T4(count=1),
    memory=1024,
    container_idle_timeout=60 * 2,
)
class EmbedBatch:
    def __enter__(self) -> None:
        self.model = get_model(setup_data)

    @web_endpoint(method="POST")
    def embed(self, payload: EmbeddingPayload):
        if payload.model != setup_data.embedding_model:
            return {"message": "model not available"}
        try:
            vecs = self.model.calc(payload.texts, payload.instruction)
            return {"message": vecs}
        except Exception as e:
            return {"message": f"error: {e}"}


@stub.cls(
    allow_concurrent_inputs=10,
    container_idle_timeout=60 * 11,
    memory=1024,
)
class EmbedSingle:
    def __enter__(self) -> None:
        self.model = get_model(setup_data)

    @web_endpoint(method="POST")
    def embed(self, payload: EmbeddingPayload):
        if payload.model != setup_data.embedding_model:
            return {"message": "model not available"}
        try:
            vecs = self.model.calc(payload.texts, payload.instruction)
            return {"message": vecs}
        except Exception as e:
            return {"message": f"error: {e}"}
