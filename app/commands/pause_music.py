from app.core.context import CommandContext

from app.music import music


class PauseMusicCommand:

    def execute(self, context: CommandContext):

        return music.pause()