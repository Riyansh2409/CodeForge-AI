from codeforge_ai.llm.openrouter import get_openrouter_model


model = get_openrouter_model()

response = model.invoke(
    "Reply with exactly: OpenRouter working"
)

print(response.content)