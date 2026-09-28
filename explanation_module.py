from gemini_client import ask_gemini


def explain_topic(topic: str) -> str:

    prompt = f"""
Explain this educational topic in simple English:

{topic}

Include:
1. Simple Definition
2. Main Points
3. Easy Example
4. Real-Life Use
5. Short Conclusion
"""

    return ask_gemini(prompt)