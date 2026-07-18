import sounddevice as sd


class Recorder:

    def __init__(self):

        self.sample_rate = 16000
        self.channels = 1

    def record(self, seconds=0.5):

        frames = int(seconds * self.sample_rate)

        audio = sd.rec(
            frames,
            samplerate=self.sample_rate,
            channels=self.channels,
            dtype="float32"
        )

        sd.wait()

        return audio