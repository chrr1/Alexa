from app.core.router import CommandRouter


class Assistant:

    def __init__(self, router: CommandRouter):
        self.router = router

    def process(self, text: str):

        return self.router.handle(text)