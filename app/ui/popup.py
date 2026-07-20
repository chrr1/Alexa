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

        self.margin = 24

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

    background:#171717;

    border:1px solid #2A2A2A;

    border-radius:18px;

}

QLabel#title{

    color:#FFFFFF;

    font-size:15px;

    font-weight:700;

    font-family:"Segoe UI Variable";

}

QLabel#status{

    color:#57E389;

    font-size:10px;

    font-weight:700;

    font-family:"Segoe UI Variable";

}

QLineEdit{

    background:#111111;

    border:1px solid #303030;

    border-radius:10px;

    color:#FFFFFF;

    padding:10px 12px;

    font-size:13px;

    font-family:"Segoe UI Variable";

    selection-background-color:#FFFFFF;

    selection-color:#000000;

}

QLineEdit::placeholder{

    color:#8A8A8A;

}

QLineEdit:focus{

    border:1px solid #FFFFFF;

}
""")

        self.show_requested.connect(self.open)

    # ================= POSISI =================

    def position(self):

        screen = self.screen().availableGeometry()

        x = screen.left() + self.margin

        y = screen.top() + self.margin

        self.move(x, y)

    # ================= OPEN =================

    def open(self):

        self.position()

        self.show()

        self.raise_()

        self.activateWindow()

        self.input.setFocus()

        self.input.selectAll()

    # ================= EXECUTE =================

    def execute(self):

        command = self.input.text().strip()

        if command:

            result = self.assistant.process(command)

            print(result)

        self.input.clear()

        self.hide()

    # ================= ESC =================

    def keyPressEvent(self, event):

        if event.key() == Qt.Key_Escape:

            self.hide()

        else:

            super().keyPressEvent(event)