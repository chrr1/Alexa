from app.music.library import MusicLibrary
from app.music.queue import MusicQueue
from app.music.player import MusicPlayer


class MusicManager:

    def __init__(self):

        self.library = MusicLibrary()

        self.queue = MusicQueue(
            self.library.all()
        )

        self.player = MusicPlayer(
            self.queue
        )

    def play(self, keyword):

        song = self.library.search(keyword)

        if song is None:
            return "Lagu tidak ditemukan."

        return self.player.play(song)

    def pause(self):

        return self.player.pause()

    def stop(self):

        return self.player.stop()

    def next(self):

        return self.player.next()

    def previous(self):

        return self.player.previous()