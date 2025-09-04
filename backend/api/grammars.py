from fastapi import APIRouter
from backend.schemas.grammar import GrammarRequest, GrammarResponse
from backend.services.grammar_service import fix_grammar


router = APIRouter(tags=["grammars"])


@router.post("/fix_grammar", response_model=GrammarResponse)
async def fix_grammar_endpoint(req: GrammarRequest):
    """Simple endpoint that returns corrected text (uses a simulated model)."""
    corrected = fix_grammar(req.text)
    return GrammarResponse(corrected=corrected)