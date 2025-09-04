from fastapi import APIRouter
from backend.schemas.coedit import CoEdITRequest, CoEdITResponse
from backend.services.coedit_service import process_text


router = APIRouter(tags=["coedits"])

@router.post("/process_text", response_model=CoEdITResponse)
async def process_text_endpoint(req: CoEdITRequest):
    """Simple endpoint that returns corrected text (uses a simulated model)."""
    improved_text = process_text(req.generate_command())
    return CoEdITResponse(
        instruction=req.instruction,
        old_text=req.text,
        improved_text=improved_text
    )
