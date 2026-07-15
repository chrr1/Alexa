import webbrowser

from app.config.website_loader import WebsiteLoader


class BrowserService:

    def __init__(self):

        self.loader = WebsiteLoader()

    def open(self, website: str):

        url = self.loader.get_url(website)

        if url is None:
            return False

        webbrowser.open(url)

        return True