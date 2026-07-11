from app.personalities.mentor import MENTOR_PROMPT
from app.personalities.friend import FRIEND_PROMPT
from app.personalities.developer import DEVELOPER_PROMPT


PERSONALITIES = {
    "Mentor": MENTOR_PROMPT,
    "Friend": FRIEND_PROMPT,
    "Senior Developer": DEVELOPER_PROMPT,
}


def get_personality_prompt(name: str):

    return PERSONALITIES.get(
        name,
        MENTOR_PROMPT
    )