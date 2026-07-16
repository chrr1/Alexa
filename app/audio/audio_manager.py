import sounddevice as sd


class AudioManager:

    def __init__(self):

        self.sample_rate = 16000
        self.channels = 1

    def list_devices(self):

        return sd.query_devices()