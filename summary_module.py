from gemini_client import ask_gemini


def summarize_text(text: str) -> str:

    prompt = f"""
You are EduGenie, an educational summarization assistant.

Summarize the following educational text:

{text}

Requirements:

- Keep the important information.
- Remove unnecessary details.
- Use simple English.
- Use clear bullet points.
- Add a short final conclusion.
"""

    return ask_gemini(prompt)