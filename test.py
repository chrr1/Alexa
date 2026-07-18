from app.voice.recorder import Recorder
from app.voice.speech_to_text import SpeechToText
from app.voice.normalizer import Normalizer

print("Memuat Whisper...")

stt = SpeechToText()
normalizer = Normalizer()
recorder = Recorder()

print("Alexa siap.\n")

while True:

    input("Tekan ENTER untuk mulai berbicara...")

    filename = recorder.record_and_save(
        "voice.wav",
        seconds=5
    )

    text = stt.transcribe(filename)

    print("\nWhisper :", text)

    text = normalizer.normalize(text)

    print("Normal :", text)
    print("-" * 40)