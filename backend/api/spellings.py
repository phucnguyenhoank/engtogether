from fastapi import APIRouter
from backend.schemas.spelling import SpellingRequest, SpellingResponse
from backend.services.spelling_service import fix_spelling_text


router = APIRouter(tags=["spellings"])

@router.post("/fix_spelling", response_model=SpellingResponse)
async def fix_spelling_ep(req: SpellingRequest):
    """Simple endpoint that returns no spelling mistake text."""
    no_spelling_text = fix_spelling_text(req.text)
    return SpellingResponse(
        old_text=req.text,
        no_spelling_text=no_spelling_text
    )
