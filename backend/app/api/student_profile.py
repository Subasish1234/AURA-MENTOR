from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.models.student_profile import StudentProfile

from app.schemas.student_profile_schema import StudentProfileCreate


router = APIRouter()


@router.post("/profile")
def create_profile(
    profile: StudentProfileCreate,
    db: Session = Depends(get_db)
):

    new_profile = StudentProfile(
        **profile.model_dump()
    )

    db.add(new_profile)

    db.commit()

    db.refresh(new_profile)

    return new_profile


@router.get("/profile/{user_id}")
def get_profile(
    user_id: int,
    db: Session = Depends(get_db)
):

    return (
        db.query(StudentProfile)
        .filter(StudentProfile.user_id == user_id)
        .first()
    )