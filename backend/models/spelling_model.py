from spellchecker import SpellChecker
import re
import Levenshtein


class SpellingModel:

    def __init__(self):
        self.spell = SpellChecker()
        self.known_words = set(self.spell.word_frequency.keys())
    
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
            token_low = token.lower()
            if token_low in misspelled:
                correction = self.spell.correction(token_low)
                
                if correction is None:
                    # None correction, fall to pure edit distance + loop through the dictionary
                    candidate_correction = token_low
                    min_edit_distance = 999
                    for candidate in self.known_words:
                        if abs(len(candidate) - len(token_low)) > 2:
                            continue
                        token_low_candidate_edit_distance = Levenshtein.distance(token_low, candidate)
                        if token_low_candidate_edit_distance < min_edit_distance:
                            min_edit_distance = token_low_candidate_edit_distance
                            candidate_correction = candidate
                    print(f'None correction for {token_low}, new candidate: {candidate_correction}')
                    corrected_tokens.append(candidate_correction)
                else:
                    corrected_tokens.append(correction) # sone rare misspelled word has None correction
            else:
                corrected_tokens.append(token)
        corrected_text = " ".join(corrected_tokens)
        # delete spacing before punctuation
        return re.sub(r"\s+([.,!?;:])", r"\1", corrected_text)
