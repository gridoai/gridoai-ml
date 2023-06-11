from pydantic import BaseModel
from uuid import UUID
import typing as t


class Document(BaseModel):
    uid: UUID
    text: str


class DatabaseCredentials(BaseModel):
    uri: str
    username: str
    password: str


class SetupData(BaseModel):
    embedding_model: str
    database_type: str
    database_credentials: DatabaseCredentials
