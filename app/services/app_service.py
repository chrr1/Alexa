import subprocess
from pathlib import Path

from app.config.app_loader import AppLoader


class AppService:

    def __init__(self):

        self.loader = AppLoader()

    def open(self, app_name: str) -> bool:

        path = self.loader.get_path(app_name)

        if path is None:
            return False

        file = Path(path)

        if not file.exists():
            return False

        subprocess.Popen([str(file)])

        return True