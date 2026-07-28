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

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)
        scroll.setObjectName("GroupFrame")
        content = QWidget()
        layout = QVBoxLayout(content)

        # Title
        layout.addWidget(QLabel(c.APP_NAME, objectName="HeaderLabel"))

        # Description
        desc = QLabel(c.t("UI_ABOUT_DESCRIPTION"))
        desc.setWordWrap(True)
        desc.setObjectName("SubtitleLabel")
        layout.addWidget(desc)

        # System info
        info = QLabel(self._sys_info())
        info.setWordWrap(True)
        info.setObjectName("SubtitleLabel")
        info.setStyleSheet("color: #888; font-family: monospace; font-size: 11px;")
        layout.addWidget(info)

        layout.addStretch(1)

        # Credits
        layout.addWidget(QLabel(c.t("UI_ABOUT_CREDITS"), objectName="SubtitleLabel",
                                alignment=Qt.AlignCenter))
        layout.addWidget(QLabel(f"{c.t('UI_VERSION_TEXT')}{c.VERSION_LAUNCHER}",
                                objectName="SubtitleLabel", alignment=Qt.AlignCenter))

        scroll.setWidget(content)
        self.main_layout.addWidget(scroll)

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
