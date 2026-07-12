from sqlalchemy.orm import Session

from app.models.conversation_history import ConversationHistory


def save_message(
    db: Session,
    user_id: int,
    role: str,
    message: str
):

    chat = ConversationHistory(
        user_id=user_id,
        role=role,
        message=message
    )

    db.add(chat)
    db.commit()