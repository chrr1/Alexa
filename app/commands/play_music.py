from app.core.context import CommandContext

from app.music import music


class PlayMusicCommand:

    def execute(self, context: CommandContext):

        if not context.arguments:

            return "Masukkan nama lagu."

        keyword = " ".join(context.arguments)

        return music.play(keyword)