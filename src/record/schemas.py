from pydantic import BaseModel, Field


class Audio(BaseModel):
    class Config:
        orm_mode = True


class AudioGET(Audio):
    id: int = Field(ge=1)
    user_id: int = Field(ge=1)
