from dotenv import load_dotenv
import os

load_dotenv()

PROJECT_NAME = os.getenv("PROJECT_NAME")

API_VERSION = os.getenv("API_VERSION")

OLLAMA_URL = os.getenv("OLLAMA_URL")

DEFAULT_MODEL = os.getenv("DEFAULT_MODEL")

SECRET_KEY = os.getenv("SECRET_KEY")

DATABASE_URL = os.getenv("DATABASE_URL")

LOG_LEVEL = os.getenv("LOG_LEVEL")

ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60)
)