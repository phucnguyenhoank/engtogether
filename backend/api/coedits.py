from fastapi import APIRouter
from backend.schemas.coedit import CoEdITRequest, CoEdITResponse
from backend.services import coedit_service as service

router = APIRouter(tags=["coedits"])


@router.post("/fix_grammar", response_model=CoEdITResponse)
async def fix_grammar_endpoint(req: CoEdITRequest):
    improved_text = service.fix_grammar(req.text)
    return CoEdITResponse(
        instruction="Fix the grammar",
        old_text=req.text,
        improved_text=improved_text,
    )


@router.post("/simplify_text", response_model=CoEdITResponse)
async def simplify_text_endpoint(req: CoEdITRequest):
    improved_text = service.simplify_text(req.text)
    return CoEdITResponse(
        instruction="Rewrite to make this text easier to understand",
        old_text=req.text,
        improved_text=improved_text,
    )


@router.post("/make_formal", response_model=CoEdITResponse)
async def make_formal_endpoint(req: CoEdITRequest):
    improved_text = service.make_formal(req.text)
    return CoEdITResponse(
        instruction="Write this more formally",
        old_text=req.text,
        improved_text=improved_text,
    )


@router.post("/make_neutral", response_model=CoEdITResponse)
async def make_neutral_endpoint(req: CoEdITRequest):
    improved_text = service.make_neutral(req.text)
    return CoEdITResponse(
        instruction="Write in a more neutral way",
        old_text=req.text,
        improved_text=improved_text,
    )


@router.post("/paraphrase", response_model=CoEdITResponse)
async def paraphrase_endpoint(req: CoEdITRequest):
    improved_text = service.paraphrase(req.text)
    return CoEdITResponse(
        instruction="Paraphrase this",
        old_text=req.text,
        improved_text=improved_text,
    )


@router.post("/custom_edit", response_model=CoEdITResponse)
async def custom_edit_endpoint(req: CoEdITRequest):
    # Ensure user provided an instruction
    if not req.instruction:
        return CoEdITResponse(
            instruction="(missing instruction)",
            old_text=req.text,
            improved_text=req.text,  # no change
        )

    improved_text = service.custom_edit(req.text, req.instruction)
    return CoEdITResponse(
        instruction=req.instruction,
        old_text=req.text,
        improved_text=improved_text,
    )
