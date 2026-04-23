from fastapi import APIRouter
from pydantic import BaseModel
from services.rag_pipeline import generate_answer

router = APIRouter()

class ChatRequest(BaseModel):
    query: str

@router.post("/chat")
def chat(request: ChatRequest):
    answer = generate_answer(request.query)

    return {
        "query": request.query,
        "answer": answer
    }