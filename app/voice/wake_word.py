import pvporcupine


class WakeWord:

    def __init__(self, access_key):

        self.porcupine = pvporcupine.create(
            access_key=access_key,
            keywords=["alexa"]
        )

    @property
    def sample_rate(self):
        return self.porcupine.sample_rate

    @property
    def frame_length(self):
        return self.porcupine.frame_length

    def detect(self, pcm):

        result = self.porcupine.process(pcm)

        return result >= 0

    def close(self):

        self.porcupine.delete()