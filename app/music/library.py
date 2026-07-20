from app.music.scanner import MusicScanner
from app.config.music_loader import MusicLoader


class MusicLibrary:

    def __init__(self):

        config = MusicLoader().load()

        folder = config["music_folder"]

        self.songs = MusicScanner().scan(folder)

    def all(self):

        return self.songs

    def count(self):

        return len(self.songs)

    def search(self, keyword):

        keyword = keyword.lower()

        for song in self.songs:

            if keyword in song.title.lower():

                return song

        return None