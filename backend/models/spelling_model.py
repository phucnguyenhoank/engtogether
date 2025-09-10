from spellchecker import SpellChecker
import re


class SpellingModel:

    def __init__(self):
        self.spell = SpellChecker()
    
    @staticmethod
    def tokenize(text):
        tokens = re.findall(r"[\w']+|[.,!?;:]", text)
        return tokens
    
    def fix_spelling(self, text: str) -> str:
        """ 
        A text, or paragraph.
        """
        tokens = SpellingModel.tokenize(text)
        misspelled = self.spell.unknown(tokens)
        corrected_tokens = []
        for token in tokens:
            if token.lower() in misspelled:
                corrected_tokens.append(self.spell.correction(token))
            else:
                corrected_tokens.append(token)

        corrected_text = " ".join(corrected_tokens)
        # delete spacing before punctuation
        return re.sub(r"\s+([.,!?;:])", r"\1", corrected_text)
