from sqlalchemy import Column, Integer, String

from app.database.database import Base


class StudentProfile(Base):
    __tablename__ = "student_profiles"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer)

    skills = Column(String)

    weaknesses = Column(String)

    learning_style = Column(String)

    preferred_personality = Column(String)

    current_goal = Column(String)