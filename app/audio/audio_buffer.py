import numpy as np


class AudioBuffer:

    def __init__(self):
        self.buffer = None

    def set(self, audio: np.ndarray):
        self.buffer = audio

    def get(self):
        return self.buffer

    def clear(self):
        self.buffer = None

    def is_empty(self):
        return self.buffer is None