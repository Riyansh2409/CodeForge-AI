from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition

from codeforge_ai.agents.analysis import create_analysis_model
from codeforge_ai.graph.state import AgentState
from codeforge_ai.llm.gemini import get_gemini_model

from codeforge_ai.tools.github.github_tools import (
    get_repository_info,
    list_repository_files,
    read_file,
)


tools = [
    get_repository_info,
    list_repository_files,
    read_file,
]


def agent_node(state: AgentState):
    print("\n================ AGENT NODE ================")

    print("\nMESSAGES COUNT:")
    print(len(state["messages"]))

    for i, message in enumerate(state["messages"]):
        print(f"\n--- MESSAGE {i} ---")
        print("TYPE:", type(message))
        print("CONTENT:", message.content)

        if hasattr(message, "tool_calls"):
            print("TOOL CALLS:", message.tool_calls)

        if hasattr(message, "tool_call_id"):
            print("TOOL CALL ID:", message.tool_call_id)

    model = get_gemini_model()

    model_with_tools = model.bind_tools(tools)

    response = model_with_tools.invoke(
        state["messages"]
    )

    print("\nMODEL RESPONSE:")
    print(response)

    return {
        "messages": [response]
    }


def analysis_node(state: AgentState):
    model = get_gemini_model()

    analysis_model = create_analysis_model(model)

    response = analysis_model.invoke(
        state["messages"]
    )

    return {
        "analysis": response
    }


def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("agent", agent_node)
    graph.add_node("tools", ToolNode(tools))
    graph.add_node("analysis", analysis_node)

    graph.add_edge(START, "agent")

    graph.add_conditional_edges(
        "agent",
        tools_condition,
        {
            "tools": "tools",
            "__end__": "analysis",
        },
    )

    graph.add_edge("tools", "agent")
    graph.add_edge("analysis", END)

    return graph.compile()