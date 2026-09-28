from gemini_client import ask_gemini


def answer_question(question: str) -> str:

    prompt = f"""
You are EduGenie, an educational AI assistant.

A student has asked this question:

{question}

Give a clear and accurate answer.

Requirements:
- Use simple English.
- Explain clearly.
- Keep the answer concise.
- Use an example if useful.
- Do not add unnecessary information.
"""

    return ask_gemini(prompt)