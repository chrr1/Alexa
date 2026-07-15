import subprocess
import webbrowser
import time

from app.services.knowledge_service import KnowledgeService
from app.services.activity_service import ActivityService


class LauncherService:

    def __init__(self):
        self.knowledge = KnowledgeService()
        self.activity = ActivityService()

    def open(self, target: str):

        activity = self.activity.find(target)

        if activity:
            return self.open_activity(activity)

        return self.open_target(target)

    def open_activity(self, activity):

        for target in activity["targets"]:
            self.open_target(target)

        for target in targets:
            self.launcher.open(target)
            time.sleep(0.5)

        return True

    def open_target(self, target):

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