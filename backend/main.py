from fastapi import FastAPI

from app.database.database import Base, engine
import app.database.models

from app.api.users import router as user_router
from app.api.memory import router as memory_router
from app.api.student_profile import router as profile_router
from app.api.chat import router as chat_router

# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(title="AURA API")

# Register routers
app.include_router(user_router)
app.include_router(memory_router)
app.include_router(profile_router)
app.include_router(chat_router)


@app.get("/")
def root():
    return {
        "message": "AURA Backend Running"
    }