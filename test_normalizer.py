from app.audio.recorder import Recorder

recorder = Recorder()

recorder.record(3)

audio = recorder.buffer.get()

print(audio.shape)