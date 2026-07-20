import ctypes
import threading

from ctypes import wintypes

user32 = ctypes.windll.user32

WM_HOTKEY = 0x0312

MOD_ALT = 0x0001
MOD_CONTROL = 0x0002

VK_SPACE = 0x20
VK_A = 0x41


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

        ctrl_space = user32.RegisterHotKey(
            None,
            1,
            MOD_CONTROL,
            VK_SPACE
        )

        alt_a = user32.RegisterHotKey(
            None,
            2,
            MOD_ALT,
            VK_A
        )

        if not ctrl_space:
            print("Gagal register Ctrl + Space")

        if not alt_a:
            print("Gagal register Alt + A")

        if not ctrl_space and not alt_a:
            return

        print("Hotkey Ctrl + Space aktif")
        print("Hotkey Alt + A aktif")

        msg = wintypes.MSG()

        while user32.GetMessageW(
            ctypes.byref(msg),
            None,
            0,
            0
        ):

            if msg.message == WM_HOTKEY:

                if msg.wParam in (1, 2):
                    self.callback()

        user32.UnregisterHotKey(None, 1)
        user32.UnregisterHotKey(None, 2)