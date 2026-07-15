from app.core.context import CommandContext
from app.core.registry import CommandRegistry


class CommandRouter:

    def __init__(self, registry: CommandRegistry):
        self.registry = registry

    def handle(self, text: str) -> str:

        text = text.strip()

        if not text:
            return "Command kosong."

        words = text.split()
        command_name = words[0].lower()
        arguments = words[1:]

        command = self.registry.get(command_name)

        if command is None:
            return f"Command '{command_name}' tidak ditemukan."

        context = CommandContext(
            raw_text=text,
            arguments=arguments
        )

        return command.execute(context)