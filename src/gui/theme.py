"""Shared theming utilities for GenovaLauncher.

When qt6ct is active the application palette is loaded from the user's
noctalia color scheme.  All dialogs should inherit their colors from
the global palette/QSS instead of hard-coding hex values.
"""
import os
from PySide6.QtGui import QPalette, QColor
from src import constants as c


def is_qt6ct():
    """Return True if the qt6ct platform theme is active."""
    return os.environ.get("QT_QPA_PLATFORMTHEME", "").lower() == "qt6ct"


def load_qt6ct_palette():
    """Parse the qt6ct color scheme file and return a QPalette.

    Qt6 palette role order (21 entries):
    WindowText, Button, Light, Midlight, Dark, Mid, Text, BrightText,
    ButtonText, Base, Window, Shadow, Highlight, HighlightedText, Link,
    LinkVisited, AlternateBase, NO_IDEA, ToolTipBase, ToolTipText,
    PlaceholderText
    """
    qt6ct_conf = os.path.join(c.HOME_DIR, ".config", "qt6ct", "qt6ct.conf")
    if not os.path.exists(qt6ct_conf):
        return None

    # Read color_scheme_path from qt6ct.conf
    scheme_path = None
    try:
        with open(qt6ct_conf, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("color_scheme_path="):
                    scheme_path = line.split("=", 1)[1].strip()
                    break
    except Exception:
        return None

    if not scheme_path or not os.path.exists(scheme_path):
        return None

    # Parse the color scheme
    colors = []
    try:
        with open(scheme_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("active_colors="):
                    raw = line.split("=", 1)[1]
                    colors = [col.strip() for col in raw.split(",") if col.strip().startswith("#")]
                    break
    except Exception:
        return None

    if len(colors) < 21:
        return None

    palette = QPalette()
    # Map to QPalette roles
    role_map = [
        QPalette.WindowText,      # 0
        QPalette.Button,          # 1
        QPalette.Light,           # 2
        QPalette.Midlight,        # 3
        QPalette.Dark,            # 4
        QPalette.Mid,             # 5
        QPalette.Text,            # 6
        QPalette.BrightText,      # 7
        QPalette.ButtonText,      # 8
        QPalette.Base,            # 9
        QPalette.Window,          # 10
        QPalette.Shadow,          # 11
        QPalette.Highlight,       # 12
        QPalette.HighlightedText, # 13
        QPalette.Link,            # 14
        QPalette.LinkVisited,     # 15
        QPalette.AlternateBase,   # 16
        # 17 = NO_IDEA -> skip
        QPalette.ToolTipBase,     # 18
        QPalette.ToolTipText,     # 19
        QPalette.PlaceholderText, # 20
    ]
    for i, role in enumerate(role_map):
        palette.setColor(QPalette.Active, role, QColor(colors[i]))
        palette.setColor(QPalette.Inactive, role, QColor(colors[i]))

    # Disabled colors (second line in scheme)
    try:
        with open(scheme_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("disabled_colors="):
                    raw = line.split("=", 1)[1]
                    disabled = [col.strip() for col in raw.split(",") if col.strip().startswith("#")]
                    if len(disabled) >= 21:
                        for i, role in enumerate(role_map):
                            palette.setColor(QPalette.Disabled, role, QColor(disabled[i]))
                    break
    except Exception:
        pass

    return palette


def apply_palette_to_app(app):
    """Load the qt6ct palette and apply it to the QApplication instance.
    Returns True if the palette was successfully loaded."""
    palette = load_qt6ct_palette()
    if palette:
        app.setPalette(palette)
        # Clear any QSS so the palette takes full effect
        try:
            app.setStyleSheet("")
        except Exception:
            pass
        return True
    return False
