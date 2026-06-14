from sqlalchemy.orm import Session

from app.models.conversation_memory import ConversationMemory


def create_memory(
    db: Session,
    user_id: int,
    memory_type: str,
    content: str
):

    memory = ConversationMemory(
        user_id=user_id,
        memory_type=memory_type,
        content=content
    )

    db.add(memory)
    db.commit()
    db.refresh(memory)

    return memory