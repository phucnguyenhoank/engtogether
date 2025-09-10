from transformers import AutoTokenizer, T5ForConditionalGeneration


class CoEdITModel:
    
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("grammarly/coedit-large")
        self.model = T5ForConditionalGeneration.from_pretrained("grammarly/coedit-large")
        self.instruction = "Rewrite to make this easier to understand"

    def edit_sentence(self, text: str) -> str:
        """
        text = 'What is you name?' (one sentence only)
        """
        input_ids = self.tokenizer(text, return_tensors="pt").input_ids
        outputs = self.model.generate(input_ids, max_length=256)
        edited_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return edited_text
