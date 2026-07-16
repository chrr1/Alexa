import sounddevice as sd

from app.audio.audio_buffer import AudioBuffer


class Recorder:

    def __init__(self):

        self.sample_rate = 16000
        self.channels = 1

        self.buffer = AudioBuffer()

    def record(self, seconds=5):

        print(f"Mendengarkan {seconds} detik...")

        audio = sd.rec(
            int(seconds * self.sample_rate),
            samplerate=self.sample_rate,
            channels=self.channels,
            dtype="float32"
        )

        sd.wait()

        self.buffer.set(audio)

        print("Audio masuk ke buffer.")

        return audio