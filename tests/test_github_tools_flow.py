from langchain_core.messages import HumanMessage, ToolMessage

from codeforge_ai.llm.openrouter import get_openrouter_model

from codeforge_ai.tools.github.github_tools import (
    get_repository_info,
    list_repository_files,
)


tools = [
    get_repository_info,
    list_repository_files,
]

model = get_openrouter_model()

model_with_tools = model.bind_tools(tools)


messages = [
    HumanMessage(
        content=(
            "Analyze the GitHub repository "
            "Riyansh2409/AI-Resume-Analyzer. "
            "First get repository information, "
            "then list its files."
        )
    )
]


# FIRST LLM CALL
response = model_with_tools.invoke(messages)

print("\nFIRST RESPONSE:")
print(response)

messages.append(response)


# EXECUTE FIRST TOOL
tool_call = response.tool_calls[0]

tool_result = get_repository_info.invoke(
    tool_call["args"]
)

print("\nFIRST TOOL RESULT:")
print(tool_result)

messages.append(
    ToolMessage(
        content=str(tool_result),
        tool_call_id=tool_call["id"],
    )
)


# SECOND LLM CALL
response = model_with_tools.invoke(messages)

print("\nSECOND RESPONSE:")
print(response)

messages.append(response)


# EXECUTE SECOND TOOL
tool_call = response.tool_calls[0]

tool_result = list_repository_files.invoke(
    tool_call["args"]
)

print("\nSECOND TOOL RESULT:")
print(tool_result)

messages.append(
    ToolMessage(
        content=str(tool_result),
        tool_call_id=tool_call["id"],
    )
)


# THIRD LLM CALL
response = model_with_tools.invoke(messages)

print("\nTHIRD RESPONSE:")
print(response)