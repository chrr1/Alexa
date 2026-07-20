from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (
    QWidget,
    QFrame,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QGraphicsDropShadowEffect
)


class AlexaPopup(QWidget):

    show_requested = Signal()

    def __init__(self, assistant):

        super().__init__()

        self.assistant = assistant

        self.setWindowFlags(
            Qt.FramelessWindowHint
            | Qt.WindowStaysOnTopHint
            | Qt.Tool
        )

        self.setAttribute(Qt.WA_TranslucentBackground)

        self.resize(200, 100)

        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)

        self.container = QFrame()
        self.container.setObjectName("container")

        shadow = QGraphicsDropShadowEffect()

        shadow.setBlurRadius(35)
        shadow.setOffset(0, 10)
        shadow.setColor(QColor(0, 0, 0, 160))

        self.container.setGraphicsEffect(shadow)

        root.addWidget(self.container)

        layout = QVBoxLayout(self.container)

        layout.setContentsMargins(18, 14, 18, 14)
        layout.setSpacing(10)

        # ================= HEADER =================

        header = QHBoxLayout()

        self.title = QLabel("Alexa")
        self.title.setObjectName("title")

        header.addWidget(self.title)

        header.addStretch()

        self.status = QLabel("● ONLINE")
        self.status.setObjectName("status")

        header.addWidget(self.status)

        layout.addLayout(header)

        # ================= INPUT =================

        self.input = QLineEdit()

        self.input.setPlaceholderText("Apa yang bisa saya bantu?")

        self.input.returnPressed.connect(self.execute)

        layout.addWidget(self.input)

        self.setStyleSheet("""

        #container{

            background:#1F2025;

            border:1px solid #32353D;

            border-radius:18px;

        }

        QLabel#title{

            color:white;

            font-size:15px;

            font-weight:700;

            font-family:"Segoe UI Variable";

        }

        QLabel#status{

            color:#57E389;

            font-size:10px;

            font-weight:bold;

            font-family:"Segoe UI Variable";

        }

        QLineEdit{

            background:#2A2D35;

            border:1px solid #3D4149;

            border-radius:10px;

            color:white;

            padding:10px 12px;

            font-size:13px;

            font-family:"Segoe UI Variable";

            selection-background-color:#4F8DFF;

        }

        QLineEdit:focus{

            border:1px solid #4F8DFF;

        }

        """)

        self.show_requested.connect(self.open)

    def center(self):

        screen = self.screen().availableGeometry()

        x = screen.center().x() - self.width() // 2

        y = 150

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

            result = self.assistant.process(command)

            print(result)

        self.input.clear()

        self.hide()

    def keyPressEvent(self, event):

        if event.key() == Qt.Key_Escape:

            self.hide()

        else:

            super().keyPressEvent(event)