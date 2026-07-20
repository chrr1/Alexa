import vlc

from app.music.queue import MusicQueue


class MusicPlayer:

    def __init__(self, queue: MusicQueue):

        self.queue = queue

        self.player = vlc.MediaPlayer()

    def play_current(self):

        song = self.queue.current()

        if song is None:
            return "Tidak ada lagu."

        media = vlc.Media(song.path)

        self.player.set_media(media)

        self.player.play()

        return f"🎵 Memutar {song.title}"

    def play(self, song):

        self.queue.jump(song)

        return self.play_current()

    def pause(self):

        self.player.pause()

        return "Pause"

    def stop(self):

        self.player.stop()

        return "Stop"

    def next(self):

        self.queue.next()

        return self.play_current()

    def previous(self):

        self.queue.previous()

        return self.play_current()