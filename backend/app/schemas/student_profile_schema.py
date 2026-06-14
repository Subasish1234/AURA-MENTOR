from pydantic import BaseModel


class StudentProfileCreate(BaseModel):

    user_id: int

    skills: str

    weaknesses: str

    learning_style: str

    preferred_personality: str

    current_goal: str