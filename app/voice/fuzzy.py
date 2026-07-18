from rapidfuzz import process

from app.voice.aliases import APP_ALIASES


class FuzzyMatcher:

    def __init__(self):

        self.words = {}

        for canonical, aliases in APP_ALIASES.items():

            for alias in aliases:

                self.words[alias] = canonical

    def fix(self, word):

        result = process.extractOne(
            word,
            self.words.keys()
        )

        if result is None:

            return word

        alias, score, _ = result

        if score >= 75:

            return self.words[alias]

        return word