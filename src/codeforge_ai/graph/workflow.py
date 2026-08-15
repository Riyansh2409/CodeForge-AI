from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition

from codeforge_ai.graph.state import AgentState
from codeforge_ai.llm.router import get_llm
from codeforge_ai.tools.github.github_tools import (
    get_repository_info,
    list_repository_files,
    read_file,
)

tools = [get_repository_info, list_repository_files, read_file,]


def agent_node(state: AgentState):
    model = get_llm()

    model_with_tools = model.bind_tools(tools)

    response = model_with_tools.invoke(state["messages"])

    return {
        "messages": [response]
    }


def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("agent", agent_node)
    graph.add_node("tools", ToolNode(tools))

    graph.add_edge(START, "agent")

    graph.add_conditional_edges(
        "agent",
        tools_condition,
    )

    graph.add_edge("tools", "agent")

    return graph.compile()