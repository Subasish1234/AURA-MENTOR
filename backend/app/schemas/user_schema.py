from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str
    degree: str
    year: str
    career_goal: str


class UserResponse(UserCreate):
    id: int

    class Config:
        from_attributes = True