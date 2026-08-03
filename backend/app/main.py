from fastapi import FastAPI
from .database import engine
from .database import Base
from . import models 
from .routers import players
from .routers import matches

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(players.router)
app.include_router(matches.router)


@app.get("/")
def home():
    return {
        "message": "Football Manager API is running"
    }