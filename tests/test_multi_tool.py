from langchain_core.messages import HumanMessage, ToolMessage
from langchain_core.tools import tool

from codeforge_ai.llm.openrouter import get_openrouter_model


@tool
def get_project_info() -> str:
    """Get project information."""
    return "CodeForge-AI is a GitHub repository analysis agent."


@tool
def list_files() -> str:
    """List project files."""
    return "main.py, workflow.py, state.py, github_tools.py"


tools = [
    get_project_info,
    list_files,
]

model = get_openrouter_model()
model_with_tools = model.bind_tools(tools)

messages = [
    HumanMessage(
        content=(
            "Analyze the CodeForge-AI project. "
            "First get project information, then list its files."
        )
    )
]

# First LLM call
response = model_with_tools.invoke(messages)

print("\nFIRST RESPONSE:")
print(response)

messages.append(response)

# Execute first tool
if response.tool_calls:
    tool_call = response.tool_calls[0]

    tool_result = get_project_info.invoke(
        tool_call["args"]
    )

    messages.append(
        ToolMessage(
            content=tool_result,
            tool_call_id=tool_call["id"],
        )
    )

# Second LLM call
response = model_with_tools.invoke(messages)

print("\nSECOND RESPONSE:")
print(response)

messages.append(response)

# Execute second tool
if response.tool_calls:
    tool_call = response.tool_calls[0]

    tool_result = list_files.invoke(
        tool_call["args"]
    )

    messages.append(
        ToolMessage(
            content=tool_result,
            tool_call_id=tool_call["id"],
        )
    )

# Third LLM call
response = model_with_tools.invoke(messages)

print("\nTHIRD RESPONSE:")
print(response)