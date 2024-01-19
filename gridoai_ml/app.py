from pydantic import BaseModel
from gridoai_ml.setup import setup_data
from fastapi import FastAPI
from gridoai_ml.text_embedding_models import get_model
from gridoai_ml.entities import Document, EmbeddingPayload
from gridoai_ml.db import get_database
from uuid import UUID
import typing as t


app = FastAPI()
model = get_model(setup_data)
database = get_database(setup_data, model.dim)


@app.post("/write")
async def write(document: Document):
    if database is None:
        return {"message": "Running without database"}
    print(f"Received document: {document}")
    vec = model.calc([document.content])[0]
    if vec is not None:
        usable_vec: t.List[float] = vec.tolist()
        database.write_vec(document, usable_vec)
        return {"message": usable_vec}
    else:
        return {"message": "error"}


@app.get("/delete")
async def delete(uid: UUID):
    if database is None:
        return {"message": "Running without database"}
    print(f"Received uid: {uid}")
    database.delete_doc(uid)


class Text(BaseModel):
    text: str


@app.post("/neardocs")
async def neardocs(text: Text):
    if database is None:
        return {"message": "Running without database"}
    print(f"Received text: {text.text}")
    vec = model.calc([text.text])[0]
    if vec is not None:
        docs = database.get_near_vecs(vec.tolist(), 10)
        return {"message": docs}
    else:
        return {"message": "error"}


@app.post("/embed")
async def embed(payload: EmbeddingPayload):
    if payload.model != setup_data.embedding_model:
        return {"message": "model not available"}
    try:
        vecs = model.calc(payload.texts, payload.instruction)
        return {"message": vecs}
    except Exception as e:
        print("failed to calculate embedding:", e)
        return {"message": "error"}
