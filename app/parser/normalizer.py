class TextNormalizer:

    REMOVE_WORDS = {

        "hai",

        "halo",

        "alexa",

        "dong",

        "tolong",

        "ya",

        "nih",

        "aku",

        "mau"
    }

    def normalize(self, text: str):

        words = []

        for word in text.lower().split():

            if word not in self.REMOVE_WORDS:

                words.append(word)

        return " ".join(words)