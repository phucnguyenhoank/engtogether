
class SimpleGrammarModel:
    """A tiny simulated model that corrects a handful of misspellings.
    It uses a mapping and replaces whole words while attempting to preserve capitalization.
    """
    def __init__(self):
        # add or extend this mapping as you like while developing
        self.mapping = {
            "teh": "the",
            "recieve": "receive",
            "langauge": "language",
            "adress": "address",
            "becuase": "because",
        }


    def correct(self, text: str) -> str:
        if text in self.mapping:
            return self.mapping[text]
        return text