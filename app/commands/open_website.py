from app.core.command import Command
from app.core.context import CommandContext
from app.services.browser_service import BrowserService


class OpenWebsiteCommand(Command):

    def __init__(self):
        self.browser = BrowserService()

    def execute(self, context: CommandContext) -> str:

        if not context.arguments:
            return "Masukkan nama website."

        website = context.arguments[0]

        if self.browser.open(website):
            return f"Membuka {website}..."

        return f"Website '{website}' tidak ditemukan."