from app.core.context import CommandContext

from app.music import music


class PreviousMusicCommand:

    def execute(self, context: CommandContext):

        return music.previous()