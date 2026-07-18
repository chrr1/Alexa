from app.voice.recorder import Recorder
from app.voice.speech_to_text import SpeechToText

print("Memuat Whisper...")

stt = SpeechToText()

print("Whisper siap.")

recorder = Recorder()

print("Mulai merekam 5 detik...")

filename = recorder.record_and_save(
    "test.wav",
    seconds=5
)

print("Rekaman selesai.")

print("Mengubah suara menjadi teks...")

text = stt.transcribe(filename)

print()
print("========== HASIL ==========")
print(text)
print("===========================")