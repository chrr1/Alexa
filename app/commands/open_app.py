from app.core.command import Command
from app.core.context import CommandContext
from app.services.launcher_service import LauncherService
from app.parser.target_parser import TargetParser


class OpenAppCommand(Command):

    def __init__(self):
        self.launcher = LauncherService()
        self.parser = TargetParser()

    def execute(self, context: CommandContext):

        if not context.arguments:
            return "Masukkan target yang ingin dibuka."

        targets = self.parser.parse(context.arguments)

        if not targets:
            return "Tidak ada target yang dapat dibuka."

        opened = []
        failed = []

        for target in targets:

            if self.launcher.open(target):
                opened.append(target)
            else:
                failed.append(target)

        message = ""

        if opened:
            message += "Membuka: " + ", ".join(opened)

        if failed:

            if message:
                message += "\n"

            message += "Tidak ditemukan: " + ", ".join(failed)

        return message