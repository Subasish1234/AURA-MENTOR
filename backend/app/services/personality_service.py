from sqlalchemy.orm import Session

from app.models.student_profile import StudentProfile


def get_user_personality(
    db: Session,
    user_id: int
):
    profile = (
        db.query(StudentProfile)
        .filter(StudentProfile.user_id == user_id)
        .first()
    )

    if not profile:
        return "Mentor"

    if not profile.preferred_personality:
        return "Mentor"

    return profile.preferred_personality