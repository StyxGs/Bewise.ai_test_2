from fastapi import FastAPI

from src.record.router import router as router_audio
from src.user.router import router as router_user

app = FastAPI()

app.include_router(router_user)
app.include_router(router_audio)
