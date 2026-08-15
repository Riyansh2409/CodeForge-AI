from codeforge_ai.llm.gemini import get_gemini_model
from codeforge_ai.llm.openrouter import get_openrouter_model
from codeforge_ai.config.settings import LLM_PROVIDER


def get_llm():
    if LLM_PROVIDER == "gemini":
        return get_gemini_model()

    if LLM_PROVIDER == "openrouter":
        return get_openrouter_model()

    raise ValueError(
        f"Unsupported LLM provider: {LLM_PROVIDER}"
    )