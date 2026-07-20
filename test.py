from app.music.manager import MusicManager

music = MusicManager()

print("Jumlah lagu :", music.library.count())

print()

print("Sedang di index awal")

print(music.current())

print()

music.jump("heaven")

print("Setelah jump")

print(music.current())

print()

print("Next")

print(music.next())

print()

print("Previous")

print(music.previous())