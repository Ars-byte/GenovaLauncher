from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel,
                             QComboBox, QScrollArea, QCheckBox, QPushButton, QFrame)
from PySide6.QtCore import Qt
from src import constants as c

class PlayTab(QWidget):
    """Main play tab with version list, launch options, and the play button."""
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        # Layout principal
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(8, 4, 8, 8)
        self.main_layout.setSpacing(6)

        # 1. Header (Game Status)
        self.header_layout = QHBoxLayout()
        self.main_layout.addLayout(self.header_layout)

        self.lbl_game_status = QLabel(c.t("UI_GAME_STATUS_IDLE"))
        self.lbl_game_status.setObjectName("SubtitleLabel")
        self.header_layout.addWidget(self.lbl_game_status)

        self.header_layout.addStretch()

        # 2. Version list title
        self.lbl_version_title = QLabel(c.t("UI_LABEL_INSTALLED_VERSIONS"))
        self.lbl_version_title.setObjectName("HeaderLabel")
        self.main_layout.addWidget(self.lbl_version_title)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setStyleSheet("border: none; background: transparent;")

        self.version_list_widget = QWidget()
        self.version_list_widget.setObjectName("VersionList")
        self.version_list_layout = QVBoxLayout(self.version_list_widget)
        self.version_list_layout.setContentsMargins(2, 2, 2, 2)
        self.version_list_layout.setSpacing(6)
        self.version_list_layout.setAlignment(Qt.AlignTop)

        self.scroll_area.setWidget(self.version_list_widget)
        self.main_layout.addWidget(self.scroll_area, 1) # Expandir

        # 3. Opciones de Lanzamiento — card con bordes
        self.opts_card = QFrame()
        self.opts_card.setObjectName("ToolCard")
        opts_card_layout = QVBoxLayout(self.opts_card)
        opts_card_layout.setContentsMargins(12, 10, 12, 10)
        opts_card_layout.setSpacing(8)

        lbl_opts_title = QLabel(c.t("UI_LAUNCH_OPTIONS"))
        lbl_opts_title.setObjectName("HeaderLabel")
        lbl_opts_title.setAlignment(Qt.AlignCenter)
        opts_card_layout.addWidget(lbl_opts_title)

        self.opts_layout = QHBoxLayout()
        self.opts_layout.setAlignment(Qt.AlignCenter)
        self.opts_layout.setSpacing(10)
        opts_card_layout.addLayout(self.opts_layout)

        self.combo_launch_action = QComboBox()
        self.combo_launch_action.addItem(c.t("UI_LAUNCH_ACTION_CLOSE"), c.LAUNCH_ACTION_CLOSE)
        self.combo_launch_action.addItem(c.t("UI_LAUNCH_ACTION_HIDE"), c.LAUNCH_ACTION_HIDE)
        self.combo_launch_action.addItem(c.t("UI_LAUNCH_ACTION_NONE"), c.LAUNCH_ACTION_NONE)
        current_action = self.app.config.get(c.CONFIG_KEY_LAUNCH_ACTION, c.LAUNCH_ACTION_CLOSE)
        idx = self.combo_launch_action.findData(current_action)
        if idx >= 0:
            self.combo_launch_action.setCurrentIndex(idx)
        self.combo_launch_action.currentIndexChanged.connect(
            lambda: self.app.sync_launch_action_ui(self.combo_launch_action.currentData())
        )
        self.opts_layout.addWidget(self.combo_launch_action)

        self.check_gamemode = QCheckBox(c.t("UI_CHECKBOX_GAMEMODE"))
        self.check_gamemode.setChecked(self.app.config.get(c.CONFIG_KEY_GAMEMODE_ENABLED, False))
        self.check_gamemode.stateChanged.connect(lambda state: self.app.sync_gamemode_ui(state == Qt.Checked.value))
        self.opts_layout.addWidget(self.check_gamemode)

        self.check_controller = QCheckBox("Controller")
        self.check_controller.setChecked(self.app.config.get("controller_enabled", False))
        self.check_controller.stateChanged.connect(
            lambda state: self.app.config_manager.set("controller_enabled", state == Qt.Checked.value)
        )
        self.opts_layout.addWidget(self.check_controller)

        if not self.app.running_in_flatpak:
            self.check_debug_log = QCheckBox(c.t("UI_CHECKBOX_DEBUG_LOG"))
            self.check_debug_log.setChecked(self.app.config.get(c.CONFIG_KEY_DEBUG_LOG, False))
            self.check_debug_log.stateChanged.connect(lambda: self.save_quick_opts())
            self.opts_layout.addWidget(self.check_debug_log)
        else:
            self.check_debug_log = None

        self.main_layout.addWidget(self.opts_card)

        # 4. Botón Jugar — card envuelto
        self.play_card = QFrame()
        self.play_card.setObjectName("ToolCard")
        play_card_layout = QVBoxLayout(self.play_card)
        play_card_layout.setContentsMargins(12, 10, 12, 10)
        play_card_layout.setSpacing(0)

        self.btn_launch = QPushButton(c.t("UI_BUTTON_PLAY_NOW"))
        self.btn_launch.setObjectName("PlayButton")
        self.btn_launch.setFixedHeight(44)
        self.btn_launch.clicked.connect(lambda: self.app.logic.launch_game(self.app))
        play_card_layout.addWidget(self.btn_launch)

        self.main_layout.addWidget(self.play_card)

        # Mock version_var for compatibility
        self._selected_version = ""

    @property
    def version_var(self):
        return self

    def get(self):
        """Return the currently selected version string."""
        return self._selected_version

    def set(self, value):
        """Set the currently selected version string."""
        self._selected_version = value

    def update_profile_indicator(self):
        """Refresh the profile indicator (kept for backward compat with external callers)."""
        pass

    def set_game_status(self, running):
        if running:
            self.lbl_game_status.setText(c.t("UI_GAME_STATUS_RUNNING"))
            self.lbl_game_status.setObjectName("StatusGreen")
        else:
            self.lbl_game_status.setText(c.t("UI_GAME_STATUS_IDLE"))
            self.lbl_game_status.setObjectName("SubtitleLabel")
        # Force QSS refresh after objectName change
        self.lbl_game_status.style().unpolish(self.lbl_game_status)
        self.lbl_game_status.style().polish(self.lbl_game_status)

    def save_quick_opts(self):
        if self.check_debug_log:
            self.app.config_manager.set(c.CONFIG_KEY_DEBUG_LOG, self.check_debug_log.isChecked())

    # Helpers to clean children (replacement for winfo_children)
    @property
    def version_listbox(self):
        return self.version_list_widget

