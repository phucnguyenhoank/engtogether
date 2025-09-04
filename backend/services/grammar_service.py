# This file contains the glue between the API and the (simulated) model.
from backend.models.grammar_model import SimpleGrammarModel


# instantiate the (very small) model once so it persists across calls
_model = SimpleGrammarModel()


def fix_grammar(text: str) -> str:
    """Call the simple model to "fix" common misspellings in `text`."""
    return _model.correct(text)