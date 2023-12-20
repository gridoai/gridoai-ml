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


@stub.function(
    gpu=gpu.T4(count=1),
    memory=1024,
)
@web_endpoint(method="POST")
async def embed_batch(payload: EmbeddingPayload):
    model = get_model(setup_data)

    if payload.model != setup_data.embedding_model:
        return {"message": "model not available"}
    try:
        vecs = model.calc(payload.texts, payload.instruction)
        return {"message": vecs}
    except:
        return {"message": "error"}


@stub.function(
    allow_concurrent_inputs=3,
    memory=1024,
)
@web_endpoint(method="POST")
async def embed_single(payload: EmbeddingPayload):
    model = get_model(setup_data)

    if payload.model != setup_data.embedding_model:
        return {"message": "model not available"}
    try:
        vecs = model.calc(payload.texts, payload.instruction)
        return {"message": vecs}
    except:
        return {"message": "error"}
