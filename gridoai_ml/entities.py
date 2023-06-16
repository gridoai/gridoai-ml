from pydantic import BaseModel
from uuid import UUID
import typing as t


class Document(BaseModel):
    uid: UUID
    path: str
    content: str


class DocumentWithDistance(Document):
    distance: float


class DatabaseCredentials(BaseModel):
    uri: str
    username: str
    password: str


class SetupData(BaseModel):
    embedding_model: str
    database_type: str
    database_credentials: DatabaseCredentials
