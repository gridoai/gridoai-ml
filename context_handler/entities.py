from pydantic import BaseModel
from uuid import UUID


class Document(BaseModel):
    uid: UUID
    text: str
