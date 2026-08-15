from langchain_core.tools import tool

from codeforge_ai.llm.openrouter import get_openrouter_model


@tool
def get_project_name() -> str:
    """Return the name of the project."""
    return "CodeForge-AI"


model = get_openrouter_model()

model_with_tools = model.bind_tools(
    [get_project_name]
)

response = model_with_tools.invoke(
    "What is the project name? Use the available tool."
)

print(response)