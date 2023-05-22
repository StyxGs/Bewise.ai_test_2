import uuid

from pydantic import BaseModel, Field


class User(BaseModel):
    class Config:
        orm_mode = True


class UserCreate(User):
    username: str = Field(max_length=100, min_length=2)


class UserRead(User):
    id: int
    token: uuid.UUID
