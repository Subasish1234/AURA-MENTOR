from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from passlib.context import CryptContext

from app.database.database import get_db
from app.database.models import User
from app.schemas.user_schema import UserCreate
from app.auth.auth import create_access_token
router = APIRouter()

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


@router.post("/register")
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    try:

        hashed_password = pwd_context.hash(
            user.password
        )

        new_user = User(
            name=user.name,
            email=user.email,
            password=hashed_password,
            degree=user.degree,
            year=user.year,
            career_goal=user.career_goal
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return {
            "message": "User registered successfully",
            "user_id": new_user.id
        }

    except IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )


@router.get("/users")
def get_users(
    db: Session = Depends(get_db)
):
    users = db.query(User).all()
    return users


@router.post("/login")
def login(
    email: str,
    password: str,
    db: Session = Depends(get_db)
):

    user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not pwd_context.verify(
        password,
        user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {"sub": user.email}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }