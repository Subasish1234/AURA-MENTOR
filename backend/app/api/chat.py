from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.chat_schema import ChatRequest

# Profile
from app.services.profile_service import get_profile_context

# Personality
from app.services.personality_service import get_user_personality

# Memory
from app.memory.memory_retriever import get_memory_context

# Conversation History
from app.history.history_service import save_message
from app.history.history_retriever import get_recent_history
from app.history.history_formatter import format_history

# Prompt Builder
from app.services.prompt_builder import build_prompt

# LLM
from app.services.llm_service import generate_response


router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post("/")
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db)
):
    """
    ==========================================================
                    AURA CHAT PIPELINE
    ==========================================================

    Workflow

    1. Save User Message

    2. Retrieve Student Profile

    3. Retrieve Long-Term Memory

    4. Retrieve Conversation History

    5. Retrieve Personality

    6. Build Prompt

    7. Generate LLM Response

    8. Save AI Response

    9. Return Response

    ==========================================================
    """

    # ----------------------------------------------------
    # Step 1 : Save User Message
    # ----------------------------------------------------

    save_message(
        db=db,
        user_id=request.user_id,
        role="User",
        message=request.message
    )

    # ----------------------------------------------------
    # Step 2 : Student Profile
    # ----------------------------------------------------

    profile_context = get_profile_context(
        db=db,
        user_id=request.user_id
    )

    # ----------------------------------------------------
    # Step 3 : Long-Term Memory
    # ----------------------------------------------------

    memory_context = get_memory_context(
        db=db,
        user_id=request.user_id
    )

    # ----------------------------------------------------
    # Step 4 : Conversation History
    # ----------------------------------------------------

    history = get_recent_history(
        db=db,
        user_id=request.user_id
    )

    conversation_history = format_history(
        history
    )

    # ----------------------------------------------------
    # Step 5 : Personality
    # ----------------------------------------------------

    personality = get_user_personality(
        db=db,
        user_id=request.user_id
    )

    # ----------------------------------------------------
    # Step 6 : Prompt Builder
    # ----------------------------------------------------

    prompt = build_prompt(
        user_message=request.message,
        profile_context=profile_context,
        memory_context=memory_context,
        conversation_history=conversation_history,
        personality=personality
    )

    # ----------------------------------------------------
    # Step 7 : Generate AI Response
    # ----------------------------------------------------

    response = generate_response(prompt)

    # ----------------------------------------------------
    # Step 8 : Save AI Response
    # ----------------------------------------------------

    save_message(
        db=db,
        user_id=request.user_id,
        role="Assistant",
        message=response
    )

    # ----------------------------------------------------
    # Step 9 : Return Response
    # ----------------------------------------------------

    return {
        "status": "success",
        "personality": personality,
        "response": response
    }