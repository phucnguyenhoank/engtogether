from gec_t5 import generate
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


class PyGECT5Model:

    def __init__(self):
        self.model = AutoModelForSeq2SeqLM.from_pretrained("gotutiyan/gec-t5-base-clang8")
        self.tokenizer = AutoTokenizer.from_pretrained("gotutiyan/gec-t5-base-clang8")
    
    def fix_spelling(self, sentences: list[str]) -> list[str]:
        predictions: list[str] = generate(
            model=self.model,
            tokenizer=self.tokenizer,
            sources=sentences,
            batch_size=32,
            retok=True,
        )
        return predictions
