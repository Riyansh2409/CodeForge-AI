from langchain_core.messages import HumanMessage

from codeforge_ai.graph.workflow import build_graph


def main():
    graph = build_graph()

    result = graph.invoke(
        {
            "messages": [
                HumanMessage(
                    content=(
                        "Analyze the GitHub repository "
                        "Riyansh2409/AI-Resume-Analyzer. "
                        "Inspect the repository structure first. "
                        "Then identify the most important source files "
                        "and read them to understand the project. "
                        "Finally, provide a concise analysis of the "
                        "architecture, technologies, and potential issues."
                    )
                )
            ],
            "analysis": None,
        }
    )

    print("\nFINAL ANALYSIS:\n")

    print(result["analysis"].model_dump_json(indent=2))


if __name__ == "__main__":
    main()