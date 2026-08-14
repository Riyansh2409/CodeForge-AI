from codeforge_ai.llm.gemini import get_gemini_model


def main():
    model = get_gemini_model()

    response = model.invoke(
        "Explain what an AI agent is in simple terms."
    )

    print(response.content)


if __name__ == "__main__":
    main()