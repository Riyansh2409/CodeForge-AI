from langchain_openai import ChatOpenAI

from codeforge_ai.config.settings import (
    OPENROUTER_API_KEY,
    OPENROUTER_MODEL,
)


def get_openrouter_model():
    return ChatOpenAI(
        model=OPENROUTER_MODEL,
        api_key=OPENROUTER_API_KEY,
        base_url="https://openrouter.ai/api/v1",
        temperature=0.2,
    )