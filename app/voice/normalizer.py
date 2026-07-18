import re

from app.voice.fuzzy import FuzzyMatcher


class Normalizer:

    def __init__(self):

        self.matcher = FuzzyMatcher()

    def normalize(self, text):

        text = text.lower()

        text = re.sub(
            r"[^\w\s]",
            "",
            text
        )

        words = text.split()

        fixed = []

        for word in words:

            fixed.append(
                self.matcher.fix(word)
            )

        return " ".join(fixed)