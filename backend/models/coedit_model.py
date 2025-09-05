from spellchecker import SpellChecker
import re

class CoEdITModel:
    """A tiny simulated model that corrects a handful of misspellings.
    It uses a mapping and replaces whole words while attempting to preserve capitalization.
    """
    def __init__(self):
        self.spell = SpellChecker(case_sensitive=True)
    
    @staticmethod
    def tokenize(text):
        tokens = re.findall(r"[\w']+|[.,!?;]", text)
        return tokens
    
    def correct(self, text: str) -> str:
        content = text.split(":")[1]
        tokens = CoEdITModel.tokenize(content)

        misspelled = self.spell.unknown(tokens)

        corrected_tokens = []
        for token in tokens:
            if token.lower() in misspelled:
                corrected_tokens.append(self.spell.correction(token))
            else:
                corrected_tokens.append(token)

        corrected_text = " ".join(corrected_tokens)
        # fix spacing before punctuation
        corrected_text = re.sub(r"\s+([.,!?;])", r"\1", corrected_text)

        return corrected_text
