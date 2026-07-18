import sounddevice as sd
import numpy as np


class Microphone:

    def __init__(self):

        info = sd.query_devices(kind="input")

        print("Menggunakan:", info["name"])

        self.sample_rate = int(info["default_samplerate"])
        self.channels = 1

    def record(self, duration):

        frames = int(duration * self.sample_rate)

        audio = sd.rec(
            frames,
            samplerate=self.sample_rate,
            channels=self.channels,
            dtype=np.int16
        )

        sd.wait()

        return audio.flatten()