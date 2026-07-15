from app.core.command import Command
from app.core.context import CommandContext
from app.services.app_service import AppService


class OpenAppCommand(Command):

    def __init__(self):

        self.app_service = AppService()

    def execute(self, context: CommandContext) -> str:

        if not context.arguments:
            return "Masukkan nama aplikasi."

        app_name = context.arguments[0]

        success = self.app_service.open(app_name)

        if success:
            return f"Membuka {app_name}..."

        return f"Aplikasi '{app_name}' tidak ditemukan."