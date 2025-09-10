from fastapi import APIRouter
from backend.schemas.coedit import CoEdITRequest, CoEdITResponse
from backend.services.coedit_service import edit_text


router = APIRouter(tags=["coedits"])

@router.post("/edit_text", response_model=CoEdITResponse)
async def edit_text_endpoint(req: CoEdITRequest):
    improved_text = edit_text(req.generate_command())
    return CoEdITResponse(
        instruction=req.instruction,
        old_text=req.text,
        improved_text=improved_text
    )
