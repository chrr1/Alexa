import json
from pathlib import Path


class WebsiteLoader:

    def __init__(self):

        project_root = Path(__file__).resolve().parents[2]

        config = project_root / "config" / "websites.json"

        with config.open(
            "r",
            encoding="utf8"
        ) as file:

            self.websites = json.load(file)

    def get_url(self, name: str):

        return self.websites.get(name.lower())