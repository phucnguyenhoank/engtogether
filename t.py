from gec_t5 import generate
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

model = AutoModelForSeq2SeqLM.from_pretrained("gotutiyan/gec-t5-base-clang8")
tokenizer = AutoTokenizer.from_pretrained("gotutiyan/gec-t5-base-clang8")

sentences = [
    "what's you name?",
    "what are you name?",
    "today is my best day in HCM, it work so great",
    "this is so   bad (good)",
    "I doesn't like you"
]

predictions: list[str] = generate(
    model=model,
    tokenizer=tokenizer,
    sources=sentences,
    batch_size=32,
    retok=True,
)
print("\n".join(predictions))
