from backend.models.pygect5_model import PyGECT5Model
from backend.utils.text_processing import split_sentences, join_sentences

_model = PyGECT5Model()

def fix_spelling_text(text: str) -> str:
    """Fix spelling mistakes in a text."""
    sentences = split_sentences(text)
    corrected_sentences = _model.fix_spelling(sentences)
    return join_sentences(corrected_sentences)
