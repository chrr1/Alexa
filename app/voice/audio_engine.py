from app.voice.recorder import Recorder


class AudioEngine:

    def __init__(self):

        self.recorder = Recorder()

    def listen(self):

        return self.recorder.record()