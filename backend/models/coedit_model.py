from transformers import AutoTokenizer, T5ForConditionalGeneration


class CoEdITModel:
    
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("grammarly/coedit-large")
        self.model = T5ForConditionalGeneration.from_pretrained("grammarly/coedit-large")

    def edit_sentence(self, text: str, instruction: str = 'Fix the grammar') -> str:
        """
        instruction = 'Fix the grammar'
        text = 'What is you name?' (one sentence only)
        """
        input_ids = self.tokenizer(f"{instruction}: {text}", return_tensors="pt").input_ids
        outputs = self.model.generate(input_ids, max_length=256)
        edited_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return edited_text
