from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel,
                             QPushButton, QScrollArea, QFrame, QGridLayout)
from PySide6.QtCore import Qt
from src import constants as c

class ToolsTab(QWidget):
    """Tools tab displaying grouped utility buttons for management, customization, files, and system tasks."""
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(4, 2, 4, 4)

        # Header
        self.header_layout = QHBoxLayout()
        self.main_layout.addLayout(self.header_layout)

        self.lbl_tools_status = QLabel("")
        self.lbl_tools_status.setObjectName("FloatingLabel")
        self.header_layout.addWidget(self.lbl_tools_status)

        self.header_layout.addStretch()

        self.lbl_current_profile = QLabel("")
        self.lbl_current_profile.setObjectName("StatusGreen")
        self.header_layout.addWidget(self.lbl_current_profile)

        # Scroll Area
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setStyleSheet("border: none; background: transparent;")

        self.scroll_content = QWidget()
        self.scroll_content.setMinimumWidth(480)
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_layout.setAlignment(Qt.AlignTop)

        self.scroll_area.setWidget(self.scroll_content)
        self.main_layout.addWidget(self.scroll_area)

        self.lbl_shader_status = None
        self.refresh_tools_ui()

    def get_tools_data(self):
        """Return the grouped tool definitions with icons, labels, and callbacks."""
        groups = [
            {
                "title": c.t("UI_SECTION_MANAGEMENT"),
                "tools": [
                    {"text": c.t("UI_BUTTON_INSTALL_APK"), "cmd": self.app.install_apk_dialog, "color": None},
                    {"text": c.t("UI_BUTTON_MANAGE_SHORTCUT"), "cmd": self.app.open_version_manager, "color": None},
                    {"text": c.t("UI_BUTTON_MIGRATE_DATA"), "cmd": self.app.open_migration_tool, "color": None},
                ]
            },
            {
                "title": c.t("UI_SECTION_CUSTOMIZATION"),
                "tools": [
                    {"text": c.t("UI_BUTTON_SKIN_PACK_CREATOR"), "cmd": self.app.open_skin_tool, "color": None},
                    {"text": c.t("UI_BUTTON_GAME_CONFIG"), "cmd": self.app.open_game_config_tool, "color": None},
                    {"text": c.t("UI_BUTTON_DISABLE_SHADERS"), "cmd": lambda: self.app.logic.disable_shaders(self.app), "color": None, "show_status": True},
                ]
            },
            {
                "title": c.t("UI_SECTION_FILES"),
                "tools": [
                    {"text": c.t("UI_BUTTON_ADDON_MANAGER"), "cmd": self.app.open_addon_manager, "color": None},
                    {"text": c.t("UI_BUTTON_OPEN_DATA_FOLDER"), "cmd": lambda: self.app.logic.open_data_folder(self.app), "color": None},
                    {"text": c.t("UI_BUTTON_OPEN_SCREENSHOTS"), "cmd": lambda: self.app.logic.export_screenshots_dialog(self.app), "color": None},
                ]
            },
            {
                "title": c.t("UI_SECTION_SYSTEM"),
                "tools": [
                    {
                        "text": c.t("UI_BUTTON_VERIFY_DEPS_FLATPAK") if self.app.running_in_flatpak else c.t("UI_BUTTON_VERIFY_DEPS_LOCAL"),
                        "cmd": lambda: self.app.logic.verify_dependencies(self.app), "color": None
                    },
                    {"text": c.t("UI_BUTTON_VERIFY_HW"), "cmd": lambda: self.app.logic.check_requirements_dialog(self.app), "color": None},
                    {"text": c.t("UI_LABEL_COMPATIBLE_RANGE"), "cmd": None, "show_compat": True}
                ]
            }
        ]
        return groups

    def refresh_tools_ui(self):
        """Rebuild the tools area, honoring the current layout style (list, columns, or grid)."""
        # Clear layout safely
        from src.core.ui_utils import clear_layout
        clear_layout(self.scroll_layout)

        layout_style = self.app.config.get(c.CONFIG_KEY_TOOLS_LAYOUT, c.STYLE_COLUMNS)
        groups = self.get_tools_data()

        if layout_style == c.STYLE_LIST:
            self._render_list(groups)
        elif layout_style == c.STYLE_COLUMNS:
            self._render_columns(groups)
        else: # GRID
            self._render_grid(groups)

        # Footer Credits
        footer = QLabel(c.t("UI_ABOUT_CREDITS"))
        footer.setObjectName("SubtitleLabel")
        footer.setAlignment(Qt.AlignCenter)
        self.scroll_layout.addWidget(footer)

    def _make_card(self, parent_layout):
        """Create a minimal card frame wrapper and return its inner layout."""
        card = QFrame()
        card.setObjectName("ToolCard")
        inner = QVBoxLayout(card)
        inner.setContentsMargins(8, 6, 8, 6)
        inner.setSpacing(4)
        parent_layout.addWidget(card)
        return inner

    def _create_tool_button(self, parent_layout, tool):
        if tool.get("show_compat"):
            inner = self._make_card(parent_layout)

            t1 = QLabel(tool["text"])
            t1.setObjectName("SubtitleLabel")
            t1.setAlignment(Qt.AlignCenter)
            inner.addWidget(t1)

            range_val_text = self.app.logic.get_compatibility_range(self.app)
            t2 = QLabel(range_val_text)
            t2.setObjectName("StatusGreen")
            t2.setStyleSheet("font-size: 13px;")
            t2.setAlignment(Qt.AlignCenter)
            inner.addWidget(t2)
            return

        if tool.get("show_drm_status"):
            inner = self._make_card(parent_layout)

            t1 = QLabel(tool["text"])
            t1.setObjectName("SubtitleLabel")
            t1.setAlignment(Qt.AlignCenter)
            inner.addWidget(t1)

            drm_status = self.app.logic.get_drm_mod_status(self.app)
            if drm_status == "installed":
                status_text = c.t("UI_DRM_MOD_STATUS_INSTALLED")
                status_color = c.COLOR_PRIMARY_GREEN
            elif drm_status == "disabled":
                status_text = c.t("UI_DRM_MOD_STATUS_DISABLED")
                status_color = c.COLOR_YELLOW_BUTTON
            else:
                status_text = c.t("UI_DRM_MOD_STATUS_MISSING")
                status_color = c.COLOR_RED_BUTTON
            t2 = QLabel(status_text)
            t2.setStyleSheet(f"color: {status_color}; font-weight: bold; font-size: 13px;")
            t2.setAlignment(Qt.AlignCenter)
            inner.addWidget(t2)

            desc = QLabel(c.t("UI_DRM_MOD_DESC"))
            desc.setWordWrap(True)
            desc.setObjectName("SubtitleLabel")
            desc.setAlignment(Qt.AlignCenter)
            inner.addWidget(desc)

            credit = QLabel(c.t("UI_DRM_MOD_CREDIT"))
            credit.setWordWrap(True)
            credit.setObjectName("SubtitleLabel")
            credit.setStyleSheet("font-style: italic;")
            credit.setAlignment(Qt.AlignCenter)
            inner.addWidget(credit)
            return

        # Regular tool → capsule button inside a card
        inner = self._make_card(parent_layout)

        btn = QPushButton(tool['text'])
        btn.setFixedHeight(c.BTN_HEIGHT)

        if tool.get("color"):
            bg = tool['color']
            r = int(bg[1:3], 16); g = int(bg[3:5], 16); b = int(bg[5:7], 16)
            luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255
            text_color = "#FFFFFF" if luminance > 0.5 else "#1a1a1a"
            btn.setStyleSheet(
                f"QPushButton {{ background-color: {bg}; color: {text_color}; "
                f"border-radius: {c.BTN_HEIGHT // 2}px; border: none; padding: 4px 18px; }}"
                f"QPushButton:hover {{ background-color: {bg}; }}"
            )
        else:
            btn.setObjectName("ToolButton")

        if tool["cmd"]:
            btn.clicked.connect(tool["cmd"])
        else:
            btn.setEnabled(False)
        inner.addWidget(btn)

        if tool.get("show_status"):
            self.lbl_shader_status = QLabel(c.t("UI_LABEL_SHADERS_STATUS"))
            self.lbl_shader_status.setObjectName("SubtitleLabel")
            self.lbl_shader_status.setAlignment(Qt.AlignCenter)
            inner.addWidget(self.lbl_shader_status)
            self.app.logic.update_shader_status_label(self.app)

    def _render_list(self, groups):
        for group in groups:
            frame = QFrame()
            frame.setObjectName("GroupFrame")
            layout = QVBoxLayout(frame)
            layout.setContentsMargins(10, 8, 10, 8)
            layout.setSpacing(6)

            title = QLabel(group['title'])
            title.setObjectName("HeaderLabel")
            title.setAlignment(Qt.AlignCenter)
            layout.addWidget(title)

            for tool in group["tools"]:
                self._create_tool_button(layout, tool)

            self.scroll_layout.addWidget(frame)

    def _render_columns(self, groups):
        grid = QGridLayout()
        self.scroll_layout.addLayout(grid)

        for i, group in enumerate(groups):
            frame = QFrame()
            frame.setObjectName("GroupFrame")
            frame.setMinimumHeight(180)
            layout = QVBoxLayout(frame)
            layout.setContentsMargins(10, 8, 10, 8)
            layout.setSpacing(6)

            title = QLabel(group['title'])
            title.setObjectName("HeaderLabel")
            title.setAlignment(Qt.AlignCenter)
            layout.addWidget(title)

            for tool in group["tools"]:
                self._create_tool_button(layout, tool)

            grid.addWidget(frame, i // 2, i % 2)

    def _render_grid(self, groups):
        grid = QGridLayout()
        self.scroll_layout.addLayout(grid)

        all_tools = []
        for group in groups:
            for tool in group["tools"]:
                all_tools.append(tool)

        for i, tool in enumerate(all_tools):
            btn = QPushButton(tool["text"])
            btn.setObjectName("ToolButton")
            btn.setFixedSize(170, 60)
            btn.setWordWrap(True)
            if tool["cmd"]:
                btn.clicked.connect(tool["cmd"])
            else:
                btn.setEnabled(False)

            grid.addWidget(btn, i // 3, i % 3)

            if tool.get("show_status"):
                self.lbl_shader_status = QLabel("...")
                self.lbl_shader_status.setObjectName("SubtitleLabel")
                grid.addWidget(self.lbl_shader_status, (i // 3) + 1, i % 3)
