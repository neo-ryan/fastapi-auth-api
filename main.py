from fastapi import FastAPI
from app.endpoints import user

app = FastAPI(title='Auth API')

app.include_router(user.router)