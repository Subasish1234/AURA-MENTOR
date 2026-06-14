from pydantic import BaseModel


class MemoryCreate(BaseModel):
    user_id: int
    memory_type: str
    content: str


class MemoryResponse(BaseModel):
    id: int
    user_id: int
    memory_type: str
    content: str

    class Config:
        from_attributes = True