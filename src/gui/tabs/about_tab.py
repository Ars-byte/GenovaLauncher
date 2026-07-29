from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea, QFrame
from PySide6.QtCore import Qt
from src import constants as c
import platform, sys, os

class AboutTab(QWidget):
    """Tab with launcher information, description, system info and credits."""

    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(8, 4, 8, 4)
        self.main_layout.setSpacing(8)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)
        scroll.setStyleSheet("border: none; background: transparent;")
        content = QWidget()
        layout = QVBoxLayout(content)
        layout.setSpacing(12)
        layout.setAlignment(Qt.AlignTop)

        # Title card
        title_card = self._make_card()
        title_card.layout().addWidget(QLabel(c.APP_NAME, objectName="HeaderLabel"))
        desc = QLabel(c.t("UI_ABOUT_DESCRIPTION"))
        desc.setWordWrap(True)
        desc.setObjectName("SubtitleLabel")
        title_card.layout().addWidget(desc)
        layout.addWidget(title_card)

        # System info card
        sys_card = self._make_card()
        sys_lbl = QLabel("System Information", objectName="HeaderLabel")
        sys_card.layout().addWidget(sys_lbl)
        info = QLabel(self._sys_info())
        info.setWordWrap(True)
        info.setObjectName("SubtitleLabel")
        info.setStyleSheet("color: #888; font-family: monospace; font-size: 11px;")
        sys_card.layout().addWidget(info)
        layout.addWidget(sys_card)

        layout.addStretch(1)

        # Credits card
        credit_card = self._make_card()
        credit_card.layout().addWidget(QLabel(c.t("UI_ABOUT_CREDITS"), objectName="SubtitleLabel",
                                              alignment=Qt.AlignCenter))
        credit_card.layout().addWidget(QLabel(f"{c.t('UI_VERSION_TEXT')}{c.VERSION_LAUNCHER}",
                                              objectName="SubtitleLabel", alignment=Qt.AlignCenter))
        layout.addWidget(credit_card)

        scroll.setWidget(content)
        self.main_layout.addWidget(scroll)

    def _make_card(self):
        card = QFrame()
        card.setObjectName("ToolCard")
        lay = QVBoxLayout(card)
        lay.setContentsMargins(14, 12, 14, 12)
        lay.setSpacing(6)
        return card

    def _sys_info(self):
        try:
            import PySide6
            qt = f"PySide6 {PySide6.__version__}"
        except Exception:
            qt = "PySide6 (unknown)"
        return (
            f"System: {platform.system()} {platform.release()}\n"
            f"Arch: {platform.machine()}\n"
            f"Python: {sys.version.split()[0]}\n"
            f"Qt: {qt}\n"
            f"Path: {os.path.expanduser('~/.local/share/mcpelauncher/')}"
        )
