from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.database.database import Base


class ConversationHistory(Base):
    __tablename__ = "conversation_history"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, nullable=False)

    role = Column(String, nullable=False)

    message = Column(String, nullable=False)

    timestamp = Column(
        DateTime,
        default=datetime.utcnow
    )