from fastapi import FastAPI
from app.api import auth, secrets, audit

app = FastAPI()

app.include_router(auth.router)
app.include_router(secrets.router)
