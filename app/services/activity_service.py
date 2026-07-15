from app.config.activity_loader import ActivityLoader


class ActivityService:

    def __init__(self):

        self.loader = ActivityLoader()

        self.activities = self.loader.all()

    def find(self, name: str):

        return self.activities.get(name.lower())