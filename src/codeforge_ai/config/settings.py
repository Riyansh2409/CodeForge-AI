import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL")
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "gemini")

LANGSMITH_TRACING = os.getenv("LANGSMITH_TRACING", "false")
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")
LANGSMITH_PROJECT = os.getenv("LANGSMITH_PROJECT", "codeforge-ai")

print("GEMINI KEY LOADED:", bool(GEMINI_API_KEY))
print(
    "GEMINI KEY PREFIX:",
    GEMINI_API_KEY[:8] if GEMINI_API_KEY else None
)