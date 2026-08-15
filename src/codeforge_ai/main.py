# from codeforge_ai.llm.gemini import get_gemini_model


# def main():
#     model = get_gemini_model()

#     response = model.invoke(
#         "Explain what an AI agent is in simple terms."
#     )

#     print(response.content)



# if __name__ == "__main__":
#     main()
from codeforge_ai.llm.openrouter import get_openrouter_model


def main():
    model = get_openrouter_model()

    response = model.invoke(
        "What is the capital of india ."
    )

    print(response.content)


if __name__ == "__main__":
    main()