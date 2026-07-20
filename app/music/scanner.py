from pathlib import Path

from app.music.song import Song


SUPPORTED = (
    ".mp3",
    ".wav",
    ".flac",
    ".ogg",
    ".m4a"
)


class MusicScanner:

    def scan(self, folder):

        songs = []

        folder = Path(folder)

        for file in folder.rglob("*"):

            if file.suffix.lower() in SUPPORTED:

                songs.append(
                    Song(
                        title=file.stem,
                        path=str(file)
                    )
                )

        songs.sort(key=lambda s: s.title.lower())

        return songs