from sqlalchemy.orm import Session

from app.database.models import StudentProfile


def get_profile_context(
    db: Session,
    user_id: int
):

    profile = (
        db.query(StudentProfile)
        .filter(StudentProfile.user_id == user_id)
        .first()
    )

    if not profile:
        return ""

    return f"""
Skills: {profile.skills}
Weaknesses: {profile.weaknesses}
Learning Style: {profile.learning_style}
Goal: {profile.current_goal}
Preferred Personality: {profile.preferred_personality}
"""