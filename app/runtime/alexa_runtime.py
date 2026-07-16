import time


class AlexaRuntime:

    def __init__(self, assistant):

        self.assistant = assistant
        self.running = False


    def start(self):

        self.running = True

        print("Alexa service aktif.")
        print("Status: standby")


        while self.running:

            time.sleep(1)


    def stop(self):

        self.running = False