from app.core.command import Command
from app.core.context import CommandContext
from app.services.launcher_service import LauncherService


class OpenAppCommand(Command):

    def __init__(self):
        self.launcher = LauncherService()

    def execute(self, context: CommandContext):

        if not context.arguments:
            return "Masukkan target yang ingin dibuka."

        target = " ".join(context.arguments)

        if self.launcher.open(target):
            return f"Membuka {target}..."

        return f"'{target}' tidak ditemukan."