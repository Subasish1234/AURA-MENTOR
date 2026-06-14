from pydantic import BaseModel

class MemoryCreate(BaseModel):
    user_id: int
    memory_type: str
    content: str