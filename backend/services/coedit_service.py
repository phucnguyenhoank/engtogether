from backend.models.coedit_model import CoEdITModel
import re

_model = CoEdITModel()

def split_to_sentences(text: str) -> list[str]:
    return re.split(r'(?<=\.)\s+', text)

def process_text(text: str) -> str:
    sentences = split_to_sentences(text)

    improved = []
    for sentence in sentences:
        if sentence.strip():  # skip empty strings
            improved.append(_model.correct_sentence(sentence.strip()))

    # join with a space to rebuild the text
    return " ".join(improved)