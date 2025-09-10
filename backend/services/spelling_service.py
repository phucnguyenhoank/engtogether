from backend.models.spelling_model import SpellingModel


_model = SpellingModel()


def fix_spelling_text(text: str) -> str:
    """Fix spelling mistakes in a text."""
    return _model.fix_spelling(text)
