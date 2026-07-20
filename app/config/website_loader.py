import json

from app.utils.resource import resource_path


class WebsiteLoader:

    def __init__(self):

        file = resource_path(
            "config",
            "websites.json"
        )

        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:

            self.data = json.load(f)

    def get_url(self, name):

        return self.data.get(name)