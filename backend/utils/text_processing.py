import re
from typing import List


def split_sentences(text: str) -> List[str]:
    """
    Split text into sentences using regex-based rules.
    Example: "Hello! How are you?" -> ["Hello!", "How are you?"]
    """
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    return [s for s in sentences if s]


def join_sentences(sentences: List[str]) -> str:
    """
    Join a list of sentences into a single text string.
    Ensures proper spacing between sentences.
    
    Example:
        ["Hello!", "How are you?"] -> "Hello! How are you?"
    """
    # Strip leading/trailing spaces per sentence
    cleaned = [s.strip() for s in sentences if s.strip()]
    # Join with a single space
    return " ".join(cleaned)

