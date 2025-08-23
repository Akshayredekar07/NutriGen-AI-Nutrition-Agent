from fastapi import APIRouter

router = APIRouter()

@router.post("/")
async def ingest(document: str):
    return {"status": "Document ingested"}
