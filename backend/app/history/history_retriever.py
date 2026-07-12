from sqlalchemy.orm import Session

from app.models.conversation_history import ConversationHistory


def get_recent_history(
    db: Session,
    user_id: int,
    limit: int = 10
):

    history = (
        db.query(ConversationHistory)
        .filter(
            ConversationHistory.user_id == user_id
        )
        .order_by(
            ConversationHistory.id.desc()
        )
        .limit(limit)
        .all()
    )

    history.reverse()

    return history