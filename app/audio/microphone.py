from app.audio.audio_manager import AudioManager


class Microphone:

    def __init__(self):

        self.audio = AudioManager()

    def show_devices(self):

        devices = self.audio.list_devices()

        for index, device in enumerate(devices):

            print(f"{index} : {device['name']}")