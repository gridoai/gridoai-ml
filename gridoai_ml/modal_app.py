from modal import Stub, web_endpoint, Secret, Image
from modal.gpu import T4
from gridoai_ml.entities import Document, EmbeddingPayload


def download_model():
    from sentence_transformers import SentenceTransformer
    get_model(setup_data)

image = Image.debian_slim().pip_install(
    # scraping pkgs
    "python-dotenv~=1.0.0",
    "requests~=2.31.0",
    "numpy",
    "sentence_transformers"
).env(
    {"SENTENCE_TRANSFORMERS_HOME":"./.cache/",
    "EMBEDDING_MODEL":"multilingual-e5-base"},
).run_function(download_model)
stub = Stub(
    name="example-get-started",
    image=image,
)

from gridoai_ml.setup import setup_data
from gridoai_ml.text_embedding_models import get_model
model = get_model(setup_data)

@stub.function(secret=Secret.from_name("my-custom-secret"), gpu='t4', allow_concurrent_inputs=3, memory=1024)
@web_endpoint("POST")
async def embed(payload: EmbeddingPayload):

    if payload.model != setup_data.embedding_model:
        return {"message": "model not available"}
    try:
        vecs = model.calc(payload.texts, payload.instruction)
        return {"message": [vec.tolist() for vec in vecs]}
    except:
        return {"message": "error"}