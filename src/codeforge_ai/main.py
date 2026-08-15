from codeforge_ai.llm.router import get_llm


def main():
    model = get_llm()

    response = model.invoke(
        "Explain Linear Regression is in simple terms."
    )

    print(response.content)


if __name__ == "__main__":
    main()