
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from main import ask_question


app = FastAPI(
    title="Financial RAG Assistant API",
    description="Financial annual report question-answering system",
    version="2.0.0"
)


# Request format
class QuestionRequest(BaseModel):
    question: str = Field(min_length=1)


# Health endpoint
@app.get("/health")
def health_check():

    return {
        "status": "healthy",
        "message": "Financial RAG Assistant API is running"
    }


# Question-answering endpoint
@app.post("/ask")
def ask_financial_question(request: QuestionRequest):

    if not request.question.strip():
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty"
        )

    try:

        result = ask_question(request.question)

        return {
            "question": request.question,
            "answer": result["answer"],
            "sources": result["sources"]
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
