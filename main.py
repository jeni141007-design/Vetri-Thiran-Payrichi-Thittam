from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from qa_module import answer_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import create_learning_path


app = FastAPI(
    title="EduGenie",
    description="Google Gemini Powered Learning Assistant",
    version="1.0.0"
)


app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.post("/api/ask")
async def ask_question_api(request: Request):

    try:
        data = await request.json()

        question = data.get("question", "").strip()

        if not question:
            return JSONResponse(
                status_code=400,
                content={
                    "success": False,
                    "message": "Please enter a question."
                }
            )

        result = answer_question(question)

        return {
            "success": True,
            "feature": "Question & Answer",
            "result": result
        }

    except Exception as error:

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": str(error)
            }
        )


@app.post("/api/explain")
async def explain_topic_api(request: Request):

    try:
        data = await request.json()

        topic = data.get("topic", "").strip()

        if not topic:
            return JSONResponse(
                status_code=400,
                content={
                    "success": False,
                    "message": "Please enter a topic."
                }
            )

        result = explain_topic(topic)

        return {
            "success": True,
            "feature": "Concept Explanation",
            "result": result
        }

    except Exception as error:

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": str(error)
            }
        )


@app.post("/api/quiz")
async def quiz_api(request: Request):

    try:
        data = await request.json()

        topic = data.get("topic", "").strip()

        if not topic:
            return JSONResponse(
                status_code=400,
                content={
                    "success": False,
                    "message": "Please enter a topic."
                }
            )

        result = generate_quiz(topic)

        return {
            "success": True,
            "feature": "Quiz Generator",
            "result": result
        }

    except Exception as error:

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": str(error)
            }
        )


@app.post("/api/summary")
async def summary_api(request: Request):

    try:
        data = await request.json()

        text = data.get("text", "").strip()

        if not text:
            return JSONResponse(
                status_code=400,
                content={
                    "success": False,
                    "message": "Please enter some text."
                }
            )

        result = summarize_text(text)

        return {
            "success": True,
            "feature": "Text Summary",
            "result": result
        }

    except Exception as error:

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": str(error)
            }
        )


@app.post("/api/learning-path")
async def learning_path_api(request: Request):

    try:
        data = await request.json()

        topic = data.get("topic", "").strip()

        if not topic:
            return JSONResponse(
                status_code=400,
                content={
                    "success": False,
                    "message": "Please enter a topic."
                }
            )

        result = create_learning_path(topic)

        return {
            "success": True,
            "feature": "Personalized Learning Path",
            "result": result
        }

    except Exception as error:

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": str(error)
            }
        )


@app.get("/api/health")
async def health_check():

    return {
        "status": "running",
        "application": "EduGenie",
        "gemini_model": "configured",
        "local_model": "configured"
    }