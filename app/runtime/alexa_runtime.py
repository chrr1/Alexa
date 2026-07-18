import time

from app.audio.recorder import Recorder
from app.runtime.runtime_state import RuntimeState


class AlexaRuntime:

    def __init__(self, assistant):

        self.assistant = assistant

        self.recorder = Recorder()

        self.running = False

        self.state = RuntimeState.STANDBY

    def start(self):

        self.running = True

        print("Alexa Runtime Aktif")

        while self.running:

            print(f"\nState : {self.state.value}")

            if self.state == RuntimeState.STANDBY:

                audio = self.recorder.record()

                print("Audio diterima")

                self.state = RuntimeState.LISTENING

            elif self.state == RuntimeState.LISTENING:

                print("Memproses audio...")

                time.sleep(1)

                self.state = RuntimeState.STANDBY

    def stop(self):

        self.running = False