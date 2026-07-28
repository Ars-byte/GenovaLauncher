# ==========================================
# MAPA DE DEPENDENCIAS DEL SISTEMA
# ==========================================
DEPENDENCY_MAP = {
    "APT": [
        "libcurl4t64", "libssl3t64", "libx11-6", "libxext6", "libxi6",
        "libxrandr2", "libxcursor1", "libxfixes3", "libxrender1",
        "libasound2t64", "libpulse0", "libsystemd0",
        "libgl1", "libegl1", "libgles2",
        "libgl1-mesa-dri", "mesa-vulkan-drivers",
        "libudev1", "libevdev2",
        "libpng16-16t64", "zlib1g",
        "libdbus-1-3",
        "libxkbcommon0", "libfontconfig1", "libfreetype6",
        "libgbm1", "libdrm2",
        "libzip4t64",
        "libqt6core6t64", "libqt6gui6t64", "libqt6widgets6t64",
        "libqt6network6t64",
        "libqt6webenginecore6", "libqt6webenginewidgets6",
        "libqt6qml6", "libqt6webchannel6",
        "qml6-module-qtquick", "qml6-module-qtquick-window",
        "qml6-module-qtquick-controls", "qml6-module-qtquick-layouts",
        "zenity", "unzip"
    ],
    "DNF": [
        "libcurl", "openssl-libs", "libX11", "libXext", "libXi",
        "libXrandr", "libXcursor", "libXfixes", "libXrender", "alsa-lib",
        "pulseaudio-libs", "systemd-libs",
        "mesa-libGL", "mesa-libEGL", "mesa-libGLES",
        "mesa-dri-drivers", "mesa-vulkan-drivers",
        "libevdev", "libpng", "zlib",
        "dbus-libs",
        "libxkbcommon", "fontconfig", "freetype",
        "mesa-libgbm", "libdrm",
        "SDL3",
        "libzip",
        "qt6-qtbase", "qt6-qtwebengine", "qt6-qtdeclarative",
        "zenity", "unzip"
    ],
    "PACMAN": [
        "curl", "openssl", "libx11", "libxext", "libxi", "libxrandr",
        "libxcursor", "libxfixes", "libxrender", "alsa-lib", "pulseaudio",
        "systemd-libs",
        "libglvnd", "mesa", "vulkan-icd-loader",
        "libevdev", "libpng", "zlib",
        "dbus",
        "libxkbcommon", "fontconfig", "freetype2",
        "libdrm",
        "sdl3",
        "libzip",
        "qt6-base", "qt6-webengine", "qt6-declarative",
        "zenity", "unzip"
    ]
}


# ==========================================
# CONSTANTES GLOBALES Y CONFIGURACIÓN
# ==========================================
import os

# --- Información de la Aplicación ---
APP_NAME = "GenovaLauncher"
VERSION_LAUNCHER = "1.0.0"
BINARY_VERSION_INFO = "v1.7.4-official"  # Default for Flatpak or if not found
BINARY_VERSION_FALLBACK = "PreCompiled Binaries from mcpelauncher Github"
DEVELOPERS = "Ars-Byte"
UPDATE_NAME = "Refinements & Fixes"
CHANGELOG = f"{UPDATE_NAME}: {APP_NAME} {VERSION_LAUNCHER}"
CREDITOS = f"Desarrollado por Ars-Byte\nLauncher no oficial de Minecraft Bedrock para Linux\n{APP_NAME} v{VERSION_LAUNCHER}"
import re
from src.utils.resource_path import resource_path


def _load_legal_text():
    paths = [
        resource_path("Docs/LICENCE & TERMINOS y CONDICIONES.md"),
        os.path.join(os.path.dirname(os.path.dirname(__file__)),
                     "Docs/LICENCE & TERMINOS y CONDICIONES.md"),
    ]
    for path in paths:
        if os.path.exists(path):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    text = f.read()
                text = re.sub(r'^#+\s*', '', text, flags=re.MULTILINE)
                text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
                return text.strip()
            except Exception:
                pass
    return "(Legal text not available)"

LEGAL_TEXT = _load_legal_text()

# --- Setup Wizard Strings ---
FLATPAK_REQUIRED_RUNTIMES = [
    "org.kde.Platform//6.9",
    "io.qt.qtwebengine.BaseApp//6.9",
    "org.freedesktop.Platform.GL.default",
    "org.freedesktop.Platform.VAAPI.Intel"
]

# --- Rutas y Nombres de Archivos ---
HOME_DIR = os.path.expanduser("~")
FLATPAK_INFO_FILE = "/.flatpak-info"
DEFAULT_FLATPAK_ID = "com.genovalauncher.Launcher"
MCPELAUNCHER_FLATPAK_ID = "com.mcpelauncher.MCPELauncher"

# Rutas de datos (sin modificar la estructura existente)
FLATPAK_DATA_DIR = ".var/app"
MCPELAUNCHER_DATA_SUBDIR = "data/mcpelauncher"
LOCAL_SHARE_DIR = ".local/share/mcpelauncher"

# Nombres de archivos de configuración
CONFIG_FILE_NAME = "genovalauncher-config.json"
OLD_CONFIG_FILE_NAME = "config.json"

# Nombres de directorios
VERSIONS_DIR = "versions"
PROFILES_DIR = "profiles"
DISABLED_PACKS_DIR = "disabled_packs"
MODS_DIR = "mods"
WORLDS_DIR = "games/com.mojang/minecraftWorlds"
SCREENSHOTS_DIR = "games/com.mojang/Screenshots"
SCREENSHOTS_DIR_ALT = "games/com.mojang/screenshots"
MINECRAFT_PE_DIR_ALT = "games/com.mojang/minecraftpe"
OPTIONS_FILE = "options.txt"
BACKUP_DIR = "MCPELauncher-OLD"
APPLICATIONS_DIR = ".local/share/applications"
DESKTOP_SHORTCUT_NAME = "genovalauncher.desktop"



# (MODE_* y STYLE_* se importan desde values.py al final del archivo)


# --- Colores de la Interfaz (Paleta cálida) ---
# Accento principal
COLOR_PRIMARY_GREEN = "#8B9A6B"       # Verde cálido apagado (estados positivos)
COLOR_PRIMARY_GREEN_HOVER = "#7A8A5B"
COLOR_BLUE_BUTTON = "#A0714D"         # Marrón medio cálido (botón principal)
COLOR_RED_BUTTON = "#B84C4C"          # Rojo cálido apagado (peligro/borrar)
COLOR_RED_BUTTON_HOVER = "#9E3E3E"
COLOR_PURPLE_BUTTON = "#8B6B8B"       # Púrpura cálido apagado
COLOR_PURPLE_BUTTON_HOVER = "#7A5A7A"
COLOR_YELLOW_BUTTON = "#D4A878"       # Ámbar cálido (advertencia)
COLOR_YELLOW_BUTTON_HOVER = "#C4956A"
COLOR_GRAY_BUTTON = "#8B7D6B"         # Gris cálido
COLOR_GRAY_BUTTON_HOVER = "#7A6E5E"
COLOR_GREEN_BUTTON = "#8B9A6B"        # Verde cálido (instalar/éxito)
COLOR_GREEN_BUTTON_HOVER = "#7A8A5B"
COLOR_ORANGE_BUTTON = "#D4A878"       # Ámbar cálido (alerta)
COLOR_ORANGE_BUTTON_HOVER = "#C4956A"
COLOR_SELECTED_GREEN = "#7A5C3A"      # Marrón oscuro cálido (seleccionado)

CORNER_RADIUS = 0
RADIUS_SMALL = 0
RADIUS_TINY = 0
RADIUS_BUTTON = 0
RADIUS_INPUT = 0
BTN_HEIGHT = 32
SECTION_PADDING = 8
ELEMENT_SPACING = 4

# --- Textos de la Interfaz (UI Strings) ---
# General
THEME_COLOR_MAP = {
    "dark-brown": "#5A3921",      # Marrón oscuro
    "light-brown": "#8B4513",     # Marrón medio
    "warm-brown": "#D2691E",     # Marrón anaranjado
    "gold-brown": "#CD853F",     # Marrón dorado
    "vanilla": "#F5F5DC",         # Vainilla claro
    "vanilla-light": "#FFF8DC",   # Vainilla más claro
}
VERSION_MANIFEST_URL = "https://raw.githubusercontent.com/Ars-Byte/mcpelauncher-versiondb/master/versions.{arch}.json.min"

# ── Update checker ──
UPDATE_CHECK_URL = "https://ars-byte.github.io/GenovaLauncher/version.json"
UPDATE_CHECK_INTERVAL = 86400  # 24h between automatic checks
VERSION_WARNINGS_URL = "https://raw.githubusercontent.com/Ars-Byte/mcpelauncher-versiondb/master/version-warnings.json"


# ═══════════════════════════════════════════
#  Re-export from sub-modules
#  (Keep constants as the single namespace)
# ═══════════════════════════════════════════

from .core.values import *
from .core.config_keys import *
from .core.ui_strings import *

# Derive UI_COLOR_THEMES from THEME_COLOR_MAP to keep a single source of truth
UI_COLOR_THEMES = list(THEME_COLOR_MAP.keys())

# ── Translation lookup (fallback; overridden by language_manager at startup) ──
_FORMAT_VARS = {
    "VERSION_LAUNCHER": VERSION_LAUNCHER,
    "APP_NAME": APP_NAME,
}


def _t_fallback(key, **kwargs):
    val = globals().get(key, f"!{key}!")
    if isinstance(val, str):
        try:
            val = val.format(**_FORMAT_VARS)
        except (KeyError, ValueError):
            pass
        if kwargs:
            try:
                val = val.format(**kwargs)
            except KeyError:
                pass
    return val

t = _t_fallback
