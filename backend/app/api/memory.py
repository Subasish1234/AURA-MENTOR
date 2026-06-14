from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.database.models import Memory
from app.schemas.memory_schema import MemoryCreate

router = APIRouter()


@router.post("/memory")
def create_memory(
    memory: MemoryCreate,
    db: Session = Depends(get_db)
):

    new_memory = Memory(
        user_id=memory.user_id,
        memory_type=memory.memory_type,
        content=memory.content
    )

    db.add(new_memory)
    db.commit()

    return {
        "message": "Memory stored"
    }


@router.get("/memory/{user_id}")
def get_memories(
    user_id: int,
    db: Session = Depends(get_db)
):
    return (
        db.query(Memory)
        .filter(Memory.user_id == user_id)
        .all()
    )