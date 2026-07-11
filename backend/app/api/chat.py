from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.chat_schema import ChatRequest

from app.memory.memory_retriever import (
    get_memory_context
)

from app.services.prompt_builder import build_prompt


from app.services.profile_service import (
    get_profile_context
)

from app.services.llm_service import (
    generate_response
)

router = APIRouter()


@router.post("/chat")
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db)
):

    profile_context = get_profile_context(
        db,
        request.user_id
    )

    memory_context = get_memory_context(
        db,
        request.user_id
    )

    prompt = build_prompt(
        request.message,
        profile_context,
        memory_context
    )

    response = generate_response(
        prompt
    )

    return {
        "response": response
    }