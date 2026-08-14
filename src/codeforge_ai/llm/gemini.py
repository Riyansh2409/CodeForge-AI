from langchain_google_genai import ChatGoogleGenerativeAI

from codeforge_ai.config.settings import GEMINI_API_KEY


def get_gemini_model():
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=GEMINI_API_KEY,
        temperature=0.2,
    )