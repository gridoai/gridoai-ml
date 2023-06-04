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
    use_mocked_model: bool
    database_type: str
    database_credentials: DatabaseCredentials
