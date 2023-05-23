from fastapi import FastAPI
from context_handler.models import doc2vec
from pydantic import BaseModel
from uuid import UUID

app = FastAPI()

class Document(BaseModel):
    id: UUID
    text: str

@app.post("/write/")
async def write(document: Document):
    text = document.text
    vec = doc2vec.calc(text)
    return {"message": vec}


@app.get("/neardocs/")
async def neardocs(text: str):
    vec = doc2vec.calc(text)
    return {"message": vec}
