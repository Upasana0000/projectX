from fastapi import FastAPI
import models
from database import engine
from routers import items

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(items.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI project!"}
