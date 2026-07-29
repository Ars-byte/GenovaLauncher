from PySide6.QtWidgets import (QWidget, QVBoxLayout, QTextEdit, QHBoxLayout,
                             QPushButton, QLabel, QFileDialog)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont
import os
from src import constants as c
from src.utils.logger import logger as app_logger


class LogsTab(QWidget):
    """Integrated log viewer tab."""

    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(8, 4, 8, 4)

        # Header
        header = QHBoxLayout()
        title = QLabel("Logs")
        title.setObjectName("HeaderLabel")
        header.addWidget(title)
        header.addStretch()

        btn_export = QPushButton("Export")
        btn_export.setObjectName("ToolButton")
        btn_export.clicked.connect(self._export_logs)
        header.addWidget(btn_export)

        btn_refresh = QPushButton("Refresh")
        btn_refresh.setObjectName("ToolButton")
        btn_refresh.clicked.connect(self._load_logs)
        header.addWidget(btn_refresh)

        btn_clear = QPushButton("Clear")
        btn_clear.setObjectName("ToolButton")
        btn_clear.clicked.connect(self._clear_logs)
        header.addWidget(btn_clear)

        self.main_layout.addLayout(header)

        # Log viewer
        self.text_view = QTextEdit()
        self.text_view.setReadOnly(True)
        self.text_view.setFont(QFont("monospace", 10))
        self.text_view.setStyleSheet("""
            QTextEdit {
                background-color: #0d1117;
                color: #c9d1d9;
                border: 1px solid #30363d;
                border-radius: 6px;
                padding: 8px;
            }
        """)
        self.main_layout.addWidget(self.text_view)

        # Auto-refresh
        self._timer = QTimer(self)
        self._timer.timeout.connect(self._load_logs)
        self._timer.start(3000)  # every 3s

        self._load_logs()

    def _get_log_files(self):
        """Find all log files."""
        log_dirs = [
            os.path.join(os.path.expanduser("~"), ".local", "share", "mcpelauncher"),
            os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
                os.path.abspath(__file__)))), "logs"),
        ]
        files = []
        for d in log_dirs:
            if os.path.isdir(d):
                for f in sorted(os.listdir(d), reverse=True):
                    if f.endswith(".log") or f.endswith(".txt"):
                        files.append(os.path.join(d, f))
        return files

    def _load_logs(self):
        """Load the most recent log file content."""
        cursor = self.text_view.textCursor()
        pos = cursor.position()
        scrollbar = self.text_view.verticalScrollBar()
        was_at_bottom = scrollbar.value() >= scrollbar.maximum() - 10

        files = self._get_log_files()
        if not files:
            self.text_view.setPlainText("No log files found.\n\nRun the launcher with ./run.sh to generate logs.")
            return

        # Read last 200 lines from the most recent log
        log_path = files[0]
        try:
            with open(log_path, "r", errors="replace") as f:
                lines = f.readlines()
            text = "".join(lines[-200:])
            self.text_view.setPlainText(f"=== {os.path.basename(log_path)} ===\n\n{text}")
        except Exception as e:
            self.text_view.setPlainText(f"Error reading logs: {e}")

        if was_at_bottom:
            scrollbar.setValue(scrollbar.maximum())
        else:
            cursor.setPosition(pos)
            self.text_view.setTextCursor(cursor)

    def _export_logs(self):
        """Export logs to a file."""
        path, _ = QFileDialog.getSaveFileName(self, "Export Logs", "logs.txt", "Text (*.txt)")
        if path:
            try:
                files = self._get_log_files()
                with open(path, "w") as out:
                    for f in files:
                        out.write(f"=== {f} ===\n")
                        with open(f, "r", errors="replace") as inp:
                            out.write(inp.read())
                        out.write("\n\n")
            except Exception as e:
                pass

    def _clear_logs(self):
        """Clear all log files."""
        files = self._get_log_files()
        for f in files:
            try:
                open(f, "w").close()
            except Exception:
                pass
        self.text_view.setPlainText("Logs cleared.")
