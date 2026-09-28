import os
import requests
from dotenv import load_dotenv

load_dotenv()

LOCAL_MODEL = os.getenv(
    "LOCAL_MODEL",
    "llama3.2"
)

LOCAL_MODEL_URL = os.getenv(
    "LOCAL_MODEL_URL",
    "http://localhost:11434"
)


def ask_local_model(prompt: str) -> str:

    url = f"{LOCAL_MODEL_URL}/api/generate"

    payload = {
        "model": LOCAL_MODEL,
        "prompt": prompt,
        "stream": False
    }

    try:

        response = requests.post(
            url,
            json=payload,
            timeout=120
        )

        response.raise_for_status()

        data = response.json()

        return data.get(
            "response",
            "Local model did not return a response."
        ).strip()

    except requests.exceptions.ConnectionError:

        return (
            "Local AI is not running.\n\n"
            "Please start Ollama and run the local model."
        )

    except requests.exceptions.Timeout:

        return (
            "Local AI took too long to respond. "
            "Please try again."
        )

    except requests.exceptions.RequestException as error:

        return f"Local AI error: {error}"