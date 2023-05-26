from dotenv import load_dotenv

load_dotenv()
from fastapi import FastAPI
from context_handler.models import doc2vec
from context_handler.entities import Document
from context_handler.db import database

app = FastAPI()


@app.post("/write/")
async def write(document: Document):
    print(f"Received document: {document}")
    vec = doc2vec.calc(document.text)
    if vec is not None:
        database.write_vec(document.uid, vec.tolist())
        return {"message": vec}
    else:
        return {"message": "error"}


@app.get("/neardocs/")
async def neardocs(text: str):
    print(f"Received text: {text}")
    vec = doc2vec.calc(text)
    if vec is not None:
        uids = database.get_near_vecs(vec.tolist(), 10)
        return {"message": uids}
    else:
        return {"message": "error"}
