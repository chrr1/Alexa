class MusicQueue:

    def __init__(self, songs):

        self.songs = list(songs)

        self.index = 0

    def current(self):

        if not self.songs:
            return None

        return self.songs[self.index]

    def next(self):

        if not self.songs:
            return None

        self.index += 1

        if self.index >= len(self.songs):
            self.index = 0

        return self.current()

    def previous(self):

        if not self.songs:
            return None

        self.index -= 1

        if self.index < 0:
            self.index = len(self.songs) - 1

        return self.current()

    def jump(self, song):

        for i, item in enumerate(self.songs):

            if item.path == song.path:

                self.index = i

                return item

        return None

    def all(self):

        return self.songs