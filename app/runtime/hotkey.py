import ctypes
import threading

from ctypes import wintypes

user32 = ctypes.windll.user32

WM_HOTKEY = 0x0312

MOD_ALT = 0x0001
MOD_CONTROL = 0x0002
MOD_SHIFT = 0x0004

VK_SPACE = 0x20


class GlobalHotkey:

    def __init__(self, callback):

        self.callback = callback

    def start(self):

        thread = threading.Thread(
            target=self.listen,
            daemon=True
        )

        thread.start()

    def listen(self):

        success = user32.RegisterHotKey(
            None,
            1,
            MOD_CONTROL,
            VK_SPACE
        )

        if not success:

            print("Gagal register hotkey")
            return

        print("Hotkey Ctrl+Space aktif")

        msg = wintypes.MSG()

        while user32.GetMessageW(
            ctypes.byref(msg),
            None,
            0,
            0
        ):

            if msg.message == WM_HOTKEY:

                self.callback()

        user32.UnregisterHotKey(None, 1)