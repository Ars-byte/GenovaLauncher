from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QProgressBar
from PySide6.QtCore import Qt

class ProgressDialog(QDialog):
    def __init__(self, parent, title, message):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setFixedSize(450, 160)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)

        self.label = QLabel(message)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setStyleSheet("font-size: 13px;")
        layout.addWidget(self.label)

        self.progressbar = QProgressBar()
        self.progressbar.setRange(0, 0)
        self.progressbar.setMinimumWidth(380)
        layout.addWidget(self.progressbar)

    def set_message(self, text):
        self.label.setText(text)

    def close(self):
        self.accept()
