class CoEdITModel:
    """A tiny simulated model that corrects a handful of misspellings.
    It uses a mapping and replaces whole words while attempting to preserve capitalization.
    """
    def __init__(self):
        self.mapping = {
            "teh": "the",
            "recieve": "receive",
            "langauge": "language",
            "adress": "address",
            "becuase": "because",
        }

    def correct(self, text: str) -> str:
        text = text.split(":")[-1]
        words = text.split()
        corrected_words = []

        for word in words:
            # strip punctuation but remember it
            prefix = ""
            suffix = ""
            core = word

            # handle punctuation like "adress," → core="adress"
            while core and not core[0].isalnum():
                prefix += core[0]
                core = core[1:]
            while core and not core[-1].isalnum():
                suffix = core[-1] + suffix
                core = core[:-1]

            # check mapping (case-insensitive)
            replacement = self.mapping.get(core.lower(), core)

            # preserve capitalization
            if core.istitle():
                replacement = replacement.capitalize()
            elif core.isupper():
                replacement = replacement.upper()

            corrected_words.append(prefix + replacement + suffix)

        return " ".join(corrected_words)
