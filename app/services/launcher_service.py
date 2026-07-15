import subprocess
import webbrowser

from app.services.knowledge_service import KnowledgeService


class LauncherService:

    def __init__(self):

        self.knowledge = KnowledgeService()

    def open(self, target: str):

        item = self.knowledge.find(target)

        if item is None:
            return False

        if item["type"] == "app":

            subprocess.Popen(item["path"])

            return True

        if item["type"] == "website":

            webbrowser.open(item["url"])

            return True

        return False