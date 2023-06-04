from gridoai_ml.setup import setup_data
from fastapi import FastAPI
from gridoai_ml.models.doc2vec import Doc2Vec
from gridoai_ml.entities import Document
from gridoai_ml.db import get_database
from uuid import UUID


app = FastAPI()
model = Doc2Vec(setup_data.use_mocked_model)
database = get_database(setup_data)


@app.post("/write")
async def write(document: Document):
    print(f"Received document: {document}")
    vec = model.calc(document.text)
    if vec is not None:
        usable_vec = vec.tolist()
        database.write_vec(document.uid, usable_vec)
        return {"message": usable_vec}
    else:
        return {"message": "error"}


@app.get("/delete")
async def delete(uid: UUID):
    print(f"Received uid: {uid}")
    database.delete_doc(uid)


@app.get("/neardocs")
async def neardocs(text: str):
    print(f"Received text: {text}")
    vec = model.calc(text)
    if vec is not None:
        uids = database.get_near_vecs(vec.tolist(), 10)
        return {"message": uids}
    else:
        return {"message": "error"}
