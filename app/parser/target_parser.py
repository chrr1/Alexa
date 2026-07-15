class TargetParser:

    SEPARATORS = {
        ",",
        "dan",
        "sama",
        "terus",
        "lalu"
    }

    def parse(self, arguments):

        targets = []

        for word in arguments:

            word = word.strip(",").lower()

            if word in self.SEPARATORS:
                continue

            targets.append(word)

        return targets