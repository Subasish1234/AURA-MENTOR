from sqlalchemy import Column, Integer, String
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

    degree = Column(String)
    year = Column(String)
    career_goal = Column(String)
    
class Memory(Base):
    __tablename__ = "memories"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer)

    memory_type = Column(String)

    content = Column(String)
    
from app.models.student_profile import StudentProfile

from app.models.conversation_history import ConversationHistory