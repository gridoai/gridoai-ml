from pydantic import BaseModel, Field
from uuid import UUID
import typing as t


class Document(BaseModel):
    uid: UUID
    path: str
    content: str


class EmbeddingPayload(BaseModel):
    texts: t.List[str]
    model: str
    instruction: t.Optional[str] = Field(None)


class DocumentWithDistance(Document):
    distance: float


class DatabaseCredentials(BaseModel):
    uri: str
    username: str
    password: str


class SetupData(BaseModel):
    embedding_model: str
    database_type: t.Optional[str]
    database_credentials: t.Optional[DatabaseCredentials]
