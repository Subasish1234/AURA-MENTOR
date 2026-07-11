import requests

from app.core.config import (
    DEFAULT_MODEL,
    OLLAMA_URL
)


def generate_response(prompt: str):

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": DEFAULT_MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    response.raise_for_status()

    return response.json()["response"]