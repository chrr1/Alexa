import json

from app.utils.resource import resource_path


class MusicLoader:

    def load(self):

        file = resource_path(
            "config",
            "music.json"
        )

        with open(
            file,
            encoding="utf-8"
        ) as f:

            return json.load(f)