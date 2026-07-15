from app.core.assistant import Assistant
from app.core.bootstrap import create_registry
from app.core.router import CommandRouter


def main():

    registry = create_registry()

    router = CommandRouter(registry)

    assistant = Assistant(router)

    while True:

        text = input("Alexa > ")

        if text.lower() == "exit":
            break

        print(assistant.process(text))


if __name__ == "__main__":
    main()