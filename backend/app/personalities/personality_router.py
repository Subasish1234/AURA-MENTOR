from app.personalities.mentor import MENTOR_PROMPT
from app.personalities.friend import FRIEND_PROMPT
from app.personalities.developer import DEVELOPER_PROMPT
from app.personalities.career import CAREER_PROMPT
from app.personalities.researcher import RESEARCHER_PROMPT
from app.personalities.startup import STARTUP_PROMPT
from app.personalities.interviewer import INTERVIEWER_PROMPT
from app.personalities.motivator import MOTIVATOR_PROMPT

PERSONALITIES = {
    "Mentor": MENTOR_PROMPT,
    "Friend": FRIEND_PROMPT,
    "Senior Developer": DEVELOPER_PROMPT,
    "Career Coach": CAREER_PROMPT,
    "Research Partner": RESEARCHER_PROMPT,
    "Startup Advisor": STARTUP_PROMPT,
    "Interviewer": INTERVIEWER_PROMPT,
    "Motivator": MOTIVATOR_PROMPT,
}


def get_personality_prompt(name: str):
    return PERSONALITIES.get(name, MENTOR_PROMPT)