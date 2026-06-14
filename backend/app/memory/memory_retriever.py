from sqlalchemy.orm import Session

from app.models.conversation_memory import ConversationMemory


def get_user_memories(
    db: Session,
    user_id: int
):

    return (
        db.query(ConversationMemory)
        .filter(
            ConversationMemory.user_id == user_id
        )
        .all()
    )


def get_memory_context(
    db: Session,
    user_id: int
):

    memories = get_user_memories(
        db,
        user_id
    )

    context = ""

    for memory in memories:

        context += (
            f"{memory.memory_type}: "
            f"{memory.content}\n"
        )

    return context