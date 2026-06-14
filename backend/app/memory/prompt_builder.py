def build_prompt(
    user_message: str,
    memory_context: str
):

    return f"""
You are AURA Mentor.

You are a personalized AI mentor.

Student Memory:
{memory_context}

User Question:
{user_message}

Provide personalized guidance.
"""