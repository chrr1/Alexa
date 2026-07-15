from app.core.command import Command


class PingCommand(Command):

    def execute(self, text: str):

        return "Pong! Alexa siap membantu."