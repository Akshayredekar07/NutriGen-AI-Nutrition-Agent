from fastapi import APIRouter, Depends
from app.deps import nutrition_agent

router = APIRouter()

@router.post("/")
async def ask(query: str):
    return {"response": nutrition_agent.run(query)}
