from app.core.registry import CommandRegistry


class CommandRouter:

    def __init__(self, registry: CommandRegistry):
        self.registry = registry

    def handle(self, text: str):

        text = text.strip()

        if not text:
            return "Command kosong."

        words = text.split()

        command_name = words[0].lower()

        command = self.registry.get(command_name)

        if command is None:
            return "Command tidak ditemukan."

        return command.execute(text)