import soundfile as sf

from app.voice.microphone import Microphone


class Recorder:

    def __init__(self):

        self.microphone = Microphone()

    def record(self, seconds=3):

        return self.microphone.record(seconds)

    def save(self, audio, filename):

        sf.write(
            filename,
            audio,
            self.microphone.sample_rate
        )

    def record_and_save(self, filename="record.wav", seconds=3):

        audio = self.record(seconds)

        self.save(audio, filename)

        return filename