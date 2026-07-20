import sys

from PySide6.QtWidgets import QApplication

from app.runtime.hotkey import GlobalHotkey
from app.ui.popup import AlexaPopup
from app.core.bootstrap import create_assistant


def start():

    assistant = create_assistant()

    app = QApplication(sys.argv)

    popup = AlexaPopup(assistant)

    hotkey = GlobalHotkey(
        popup.show_requested.emit
    )

    hotkey.start()

    print("Alexa Launcher aktif")

    sys.exit(app.exec())


if __name__ == "__main__":
    start()