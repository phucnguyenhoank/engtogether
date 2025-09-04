from backend.models.coedit_model import CoEdITModel

_model = CoEdITModel()

def process_text(text: str) -> str:
    return _model.correct(text)