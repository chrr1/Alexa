from pathlib import Path
import json


class AppLoader:
    def __init__(self):
        project_root = Path(__file__).resolve().parents[2]

        config_file = project_root / "config" / "apps.json"

        print("Config:", config_file)
        print("Exists:", config_file.exists())

        with config_file.open("r", encoding="utf-8") as file:
            self.apps = json.load(file)

    def get_path(self, app_name: str):
        return self.apps.get(app_name.lower())