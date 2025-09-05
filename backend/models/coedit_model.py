from spellchecker import SpellChecker
from transformers import AutoTokenizer, T5ForConditionalGeneration
import re

class CoEdITModel:
    """A tiny simulated model that corrects a handful of misspellings.
    It uses a mapping and replaces whole words while attempting to preserve capitalization.
    """
    def __init__(self):
        self.spell = SpellChecker()
        self.tokenizer = AutoTokenizer.from_pretrained("grammarly/coedit-large")
        self.model = T5ForConditionalGeneration.from_pretrained("grammarly/coedit-large")
    
    @staticmethod
    def tokenize(text):
        tokens = re.findall(r"[\w']+|[.,!?;:]", text)
        return tokens
    
    def fix_spelling(self, text: str) -> str:
        tokens = CoEdITModel.tokenize(text)
        misspelled = self.spell.unknown(tokens)
        corrected_tokens = []
        for token in tokens:
            if token.lower() in misspelled:
                corrected_tokens.append(self.spell.correction(token))
            else:
                corrected_tokens.append(token)

        corrected_text = " ".join(corrected_tokens)
        # fix spacing before punctuation
        return re.sub(r"\s+([.,!?;:])", r"\1", corrected_text)
    
    def correct_sentence(self, text: str) -> str:
        """ 
        text = 'Rewrite to make this easier to understand: Today, I worked so hard,... her.'
        """
        corrected_text = self.fix_spelling(text)

        input_ids = self.tokenizer(corrected_text, return_tensors="pt").input_ids
        outputs = self.model.generate(input_ids, max_length=256)
        edited_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return edited_text
