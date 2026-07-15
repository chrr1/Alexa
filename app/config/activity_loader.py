import json
from pathlib import Path


class ActivityLoader:

    def __init__(self):

        root = Path(__file__).resolve().parents[2]

        file = root / "config" / "activities.json"

        with file.open(
            "r",
            encoding="utf-8"
        ) as f:

            self.activities = json.load(f)

    def all(self):

        return self.activities