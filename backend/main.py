from fastapi import FastAPI

from app.database.database import engine
from app.database.database import Base

import app.database.models

from app.api.users import router as user_router
from app.api.memory import router as memory_router
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AURA API")

app.include_router(user_router)


@app.get("/")
def root():
    return {
        "message": "AURA Backend Running"
    }
    
app.include_router(memory_router)