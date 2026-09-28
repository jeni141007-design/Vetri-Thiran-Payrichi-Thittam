from gemini_client import ask_gemini


def create_learning_path(topic: str) -> str:

    prompt = f"""
You are EduGenie, a personalized learning assistant.

Create a beginner-to-advanced learning path for:

{topic}

Include:

1. Beginner Level
2. Intermediate Level
3. Advanced Level
4. Suggested Timeline
5. Practice Activities
6. Mini Project Ideas
7. Final Learning Goal

Make the learning path practical for a college student.

Use simple English.
"""

    return ask_gemini(prompt)