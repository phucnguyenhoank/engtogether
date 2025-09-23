from backend.models.coedit_model import CoEdITModel
import re

_model = CoEdITModel()


def text_to_sentences(text: str) -> list[str]:
    """Split text into sentences by period + space."""
    return re.split(r'(?<=\.)\s+', text)


def fix_grammar(text: str) -> str:
    return _apply_instruction(text, "Fix the grammar")


def simplify_text(text: str) -> str:
    return _apply_instruction(text, "Rewrite to make this text easier to understand")


def make_formal(text: str) -> str:
    return _apply_instruction(text, "Write this more formally")


def make_neutral(text: str) -> str:
    return _apply_instruction(text, "Write in a more neutral way")


def make_informal(text: str) -> str:
    return _apply_instruction(text, "Make this informal")


def paraphrase(text: str) -> str:
    return _apply_instruction(text, "Paraphrase this")


def custom_edit(text: str, instruction: str) -> str:
    return _apply_instruction(text, instruction)


# ===== Helper =====
def _apply_instruction(text: str, instruction: str) -> str:
    """Apply CoEdITModel editing to each sentence with a given instruction."""
    sentences = text_to_sentences(text)

    improved = []
    for sentence in sentences:
        if sentence.strip():
            improved.append(_model.edit_sentence(sentence.strip(), instruction))

    return " ".join(improved)
