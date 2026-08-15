from codeforge_ai.llm.gemini import get_gemini_model


model = get_gemini_model()

response = model.invoke(
    "Reply with exactly: Gemini working"
)

print(response.content)