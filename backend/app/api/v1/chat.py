from fastapi import APIRouter

from app.schemas.chat import ChatRequest

from app.services.rag.rag_service import RAGService

router = APIRouter()


@router.post("/chat")

def chat(request: ChatRequest):

    rag = RAGService()

    return rag.ask(
        request.question
    )