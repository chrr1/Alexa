import sys

from PySide6.QtWidgets import QApplication

from app.runtime.hotkey import GlobalHotkey
from app.ui.popup import AlexaPopup
from app.core.bootstrap import create_assistant


assistant = create_assistant()

app = QApplication(sys.argv)

popup = AlexaPopup(assistant)

hotkey = GlobalHotkey(
    popup.show_requested.emit
)

hotkey.start()

print("Alexa Launcher aktif")

sys.exit(app.exec())