from modal import Stub, web_endpoint
from gridoai_ml.entities import Document, EmbeddingPayload


stub = Stub("example-get-started")


@stub.function()
@web_endpoint("POST")
async def embed(payload: EmbeddingPayload):
    from gridoai_ml.setup import setup_data
    from gridoai_ml.text_embedding_models import get_model

    model = get_model(setup_data)
    if payload.model != setup_data.embedding_model:
        return {"message": "model not available"}
    try:
        vecs = model.calc(payload.texts, payload.instruction)
        return {"message": [vec.tolist() for vec in vecs]}
    except:
        return {"message": "error"}
