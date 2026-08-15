from typing import Annotated, TypedDict

from langchain_core.messages import AnyMessage
from langgraph.graph.message import add_messages

from codeforge_ai.agents.analysis import RepositoryAnalysis


class AgentState(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
    analysis: RepositoryAnalysis | None