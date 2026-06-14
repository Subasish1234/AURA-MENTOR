from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from app.database.database import Base


class ConversationMemory(Base):
    __tablename__ = "conversation_memories"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, nullable=False)

    memory_type = Column(String, nullable=False)

    content = Column(Text, nullable=False)