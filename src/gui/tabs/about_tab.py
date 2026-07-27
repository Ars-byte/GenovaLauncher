from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt
from src import constants as c

class AboutTab(QWidget):
    """Tab with launcher information, description, and credits."""

    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(8, 4, 8, 4)

        # Title
        self.title_label = QLabel(c.APP_NAME)
        self.title_label.setObjectName("HeaderLabel")
        self.main_layout.addWidget(self.title_label)

        # Description (translated)
        self.desc_label = QLabel(c.t("UI_ABOUT_DESCRIPTION"))
        self.desc_label.setWordWrap(True)
        self.desc_label.setObjectName("SubtitleLabel")
        self.desc_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.main_layout.addWidget(self.desc_label)

        self.main_layout.addStretch(1)

        # Credits (translated)
        self.credits_label = QLabel(c.t("UI_ABOUT_CREDITS"))
        self.credits_label.setObjectName("SubtitleLabel")
        self.credits_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.credits_label)

        self.version_label = QLabel(
            f"{c.t('UI_VERSION_TEXT')}{c.VERSION_LAUNCHER}"
        )
        self.version_label.setObjectName("SubtitleLabel")
        self.version_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.version_label)
