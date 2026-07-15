from app.core.command import Command
from app.core.context import CommandContext


class PingCommand(Command):

    def execute(self, context: CommandContext) -> str:
        return "Pong! Alexa di sinii."