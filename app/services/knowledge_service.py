from app.config.knowledge_loader import KnowledgeLoader


class KnowledgeService:

    def __init__(self):

        self.loader = KnowledgeLoader()

        self.data = self.loader.all()

    def find(self, name: str):

        name = name.lower()

        if name in self.data:
            return self.data[name]

        for key, value in self.data.items():

            if name in value["aliases"]:
                return value

        return None