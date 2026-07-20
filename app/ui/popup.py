from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QGraphicsDropShadowEffect,
)

from PySide6.QtGui import QColor


class AlexaPopup(QWidget):

    show_requested = Signal()

    def __init__(self, assistant):

        super().__init__()

        self.assistant = assistant

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint
        )

        self.setAttribute(Qt.WA_TranslucentBackground)

        self.resize(650, 220)

        self.container = QWidget(self)

        self.container.setObjectName("container")

        self.container.setGeometry(0, 0, 650, 220)

        shadow = QGraphicsDropShadowEffect()

        shadow.setBlurRadius(40)

        shadow.setOffset(0, 12)

        shadow.setColor(QColor(0, 0, 0, 120))

        self.container.setGraphicsEffect(shadow)

        layout = QVBoxLayout()

        layout.setContentsMargins(35, 30, 35, 30)

        layout.setSpacing(18)

        title = QLabel("🤖 Alexa")

        title.setFont(QFont("Segoe UI", 20, QFont.Bold))

        title.setAlignment(Qt.AlignCenter)

        subtitle = QLabel("Apa yang bisa saya bantu hari ini?")

        subtitle.setAlignment(Qt.AlignCenter)

        subtitle.setFont(QFont("Segoe UI", 10))

        self.input = QLineEdit()

        self.input.setPlaceholderText("Cari aplikasi, website, atau ketik perintah...")

        self.input.returnPressed.connect(self.execute)

        self.input.setMinimumHeight(48)

        self.input.setFont(QFont("Segoe UI", 11))

        layout.addWidget(title)

        layout.addWidget(subtitle)

        layout.addWidget(self.input)

        self.container.setLayout(layout)

        self.setStyleSheet("""

        #container{

            background:#202123;

            border-radius:20px;

        }

        QLabel{

            color:white;

        }

        QLineEdit{

            background:#2B2D31;

            color:white;

            border:none;

            border-radius:12px;

            padding:12px;

        }

        QLineEdit:focus{

            border:2px solid #4F8CFF;

        }

        """)

        self.show_requested.connect(self.open)

    def center(self):

        screen = self.screen().availableGeometry()

        x = screen.center().x() - self.width() // 2

        y = screen.height() // 4

        self.move(x, y)

    def open(self):

        self.center()

        self.show()

        self.raise_()

        self.activateWindow()

        self.input.setFocus()

    def execute(self):

        command = self.input.text().strip()

        if command:

            print(self.assistant.process(command))

        self.input.clear()

        self.hide()

    def keyPressEvent(self, event):

        if event.key() == Qt.Key_Escape:

            self.hide()

        else:

            super().keyPressEvent(event)