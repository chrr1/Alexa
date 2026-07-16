from app.core.assistant import Assistant
from app.core.bootstrap import create_registry
from app.core.router import CommandRouter
from app.runtime.alexa_runtime import AlexaRuntime

import sys


def create_assistant():

    registry = create_registry()
    router = CommandRouter(registry)

    return Assistant(router)


def main():

    assistant = create_assistant()

    if len(sys.argv) > 1:

        mode = sys.argv[1].lower()

        if mode == "service":

            runtime = AlexaRuntime(assistant)
            runtime.start()
            return

    print("Alexa Terminal Mode")
    print("Ketik 'exit' untuk keluar.\n")

    while True:

        text = input("Alexa > ")

        if text.lower() == "exit":
            break

        print(assistant.process(text))


if __name__ == "__main__":
    main()