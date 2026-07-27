# SunshineLauncher

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![PySide6](https://img.shields.io/badge/UI-PySide6-green?style=flat-square&logo=qt&logoColor=white)](https://www.qt.io/qt-for-python)
[![Platform](https://img.shields.io/badge/Platform-Linux-FCC624?style=flat-square&logo=linux&logoColor=black)](https://www.kernel.org/)
[![License](https://img.shields.io/badge/License-GPL%20v3-red?style=flat-square)](LICENSE)

A modern graphical launcher for **Minecraft: Bedrock Edition** on Linux, built with PySide6 (Qt6) and powered by the [mcpelauncher](https://github.com/minecraft-linux/mcpelauncher-manifest) project.

---

## Features

- **Version management** — install, switch, and play multiple Minecraft Bedrock versions from APK files or Google Play
- **Google Play integration** — download versions directly from your Play Store library
- **Resource manager** — manage resource packs, behavior packs, skins, and worlds from one interface
- **Mod support** — browse and install mods from the official mcpelauncher-moddb repository
- **Independent profiles** — each profile keeps its own worlds, settings, and data via symlinks
- **Nvidia optimizations** — Nvidia Prime and Zink (OpenGL over Vulkan) support for hybrid graphics systems
- **Data migration** — import worlds, versions, and resources from other launchers
- **Hardware analysis** — checks your system compatibility before launching
- **Multi-language** — English, Spanish, German, French, Italian, Portuguese, Catalan, Japanese

---

## Requirements

- **Linux** x86_64
- **Python** 3.10 or newer
- **OpenGL ES 3.0** or higher (for modern Minecraft Bedrock versions)
- **mcpelauncher binaries** — download pre-compiled binaries from [mcpelauncher](https://github.com/minecraft-linux/mcpelauncher-manifest/releases) or build from source

### System Dependencies

```bash
# Void Linux
doas xbps-install qt6-base qt6-webengine qt6-declarative qt6-webchannel qt6-position libzip unzip zenity

# Debian/Ubuntu
sudo apt install qt6-base qt6-webengine qt6-declarative qt6-webchannel libzip unzip zenity

# Arch
sudo pacman -S qt6-base qt6-webengine qt6-declarative qt6-webchannel libzip unzip zenity
```

---

## Installation

### Portable Release

1. Download the latest `SunshineLauncher-v*.tar.gz` from [Releases](https://github.com/Ars-Byte/SunshineLauncher/releases)
2. Extract to any directory
3. Run:

```bash
./SunshineLauncher.sh
```

### From Source

```bash
git clone https://github.com/Ars-Byte/SunshineLauncher.git
cd SunshineLauncher
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
./run.sh
```

---

## Configuration

Place mcpelauncher binaries (`mcpelauncher-client`, `mcpelauncher-webview`, `msa-daemon`, `mcpelauncher-extract`) in a `bin/` directory next to the launcher, or configure their paths in Settings > Binary Paths.

For detailed usage, see the [User Manual](Docs/MANUAL%20DE%20USO.md).

---

## License

This project is licensed under the **GNU General Public License v3.0**.

**Third-party attribution** — this launcher builds upon the [mcpelauncher](https://github.com/minecraft-linux/mcpelauncher-manifest) project by ChristopherHX, MCMrARM, and contributors.

---

## Developer

**Ars-Byte**

---
<p align="center"><sub>Built for the Linux community.</sub></p>
