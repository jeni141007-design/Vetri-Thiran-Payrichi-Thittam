from gemini_client import ask_gemini


def generate_quiz(topic: str) -> str:

    prompt = f"""
You are EduGenie, an educational quiz generator.

Create a quiz about:

{topic}

Create exactly 5 multiple-choice questions.

For each question provide:

Question:
A)
B)
C)
D)
Correct Answer:

Make the questions suitable for a college student.

Do not make all correct answers the same option.
"""

    return ask_gemini(prompt)