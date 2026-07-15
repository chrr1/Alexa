import json
from pathlib import Path


class KnowledgeLoader:

    def __init__(self):

        project_root = Path(__file__).resolve().parents[2]

        file = project_root / "config" / "knowledge.json"

        with file.open(
            "r",
            encoding="utf-8"
        ) as f:

            self.data = json.load(f)

    def all(self):

        return self.data