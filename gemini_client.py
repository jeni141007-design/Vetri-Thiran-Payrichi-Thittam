import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-2.5-flash"
)

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY is missing. Please add it to the .env file."
    )

client = genai.Client(api_key=API_KEY)


def ask_gemini(prompt: str) -> str:

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt
    )

    if not response.text:
        return "Gemini did not return a response."

    return response.text.strip()