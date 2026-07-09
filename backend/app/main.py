from fastapi import FastAPI
from app.api.thermometr import thermometr_router

app = FastAPI()
app.include_router(thermometr_router)