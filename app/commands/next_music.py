from app.core.context import CommandContext

from app.music import music


class NextMusicCommand:

    def execute(self, context: CommandContext):

        return music.next()