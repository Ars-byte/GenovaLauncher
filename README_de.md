# SunshineLauncher

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![PySide6](https://img.shields.io/badge/UI-PySide6-green?style=flat-square&logo=qt&logoColor=white)](https://www.qt.io/qt-for-python)
[![Platform](https://img.shields.io/badge/Platform-Linux-FCC624?style=flat-square&logo=linux&logoColor=black)](https://www.kernel.org/)
[![License](https://img.shields.io/badge/License-GPL%20v3-red?style=flat-square)](LICENSE)

Ein moderner grafischer Launcher fur **Minecraft: Bedrock Edition** unter Linux, entwickelt mit PySide6 (Qt6) und basierend auf dem [mcpelauncher](https://github.com/minecraft-linux/mcpelauncher-manifest)-Projekt.

---

## Funktionen

- **Versionsverwaltung** — mehrere Minecraft Bedrock-Versionen installieren, wechseln und spielen, von APK-Dateien oder Google Play
- **Google Play-Integration** — Versionen direkt aus der Play Store-Bibliothek herunterladen
- **Ressourcenmanager** — Ressourcenpakete, Verhaltenspakete, Skins und Welten von einer Oberflache aus verwalten
- **Mod-Unterstutzung** — Mods aus dem offiziellen mcpelauncher-moddb-Repository durchsuchen und installieren
- **Unabhangige Profile** — jedes Profil behalt seine eigenen Welten, Einstellungen und Daten uber Symlinks
- **Nvidia-Optimierungen** — Unterstutzung fur Nvidia Prime und Zink (OpenGL uber Vulkan)
- **Datenmigration** — Welten, Versionen und Ressourcen von anderen Launchern importieren
- **Mehrsprachig** — Englisch, Spanisch, Deutsch, Franzosisch, Italienisch, Portugiesisch, Katalanisch und Japanisch

---

## Voraussetzungen

- **Linux** x86_64
- **Python** 3.10 oder hoher
- **OpenGL ES 3.0** oder hoher (fur moderne Minecraft Bedrock-Versionen)
- **mcpelauncher-Binardateien** — vorkompilierte Binardateien von [mcpelauncher](https://github.com/minecraft-linux/mcpelauncher-manifest/releases) herunterladen

### Systemabhangigkeiten

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

1. Die neueste `SunshineLauncher-v*.tar.gz` von [Releases](https://github.com/Ars-byte/Sunshine-launcher/releases) herunterladen
2. In ein beliebiges Verzeichnis entpacken
3. Ausfuhren:

```bash
./SunshineLauncher.sh
```

### Aus dem Quellcode

```bash
git clone https://github.com/Ars-byte/Sunshine-launcher.git
cd Sunshine-launcher
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
./run.sh
```

---

## Leistung

SunshineLauncher wendet automatisch Optimierungen zur Verbesserung der Spielleistung an:

- `mesa_glthread=true` — Multithreaded GL-Dispatch fur Intel/AMD-GPUs
- Persistenten Shader-Cache (`~/.cache/sunshine-shaders/`)
- `MESA_NO_ERROR=1` — uberspringt GL-Fehlerprufungen in der Produktion
- `ANV_SPARSE=1` — Sparse Memory fur den Intel ANV Vulkan-Treiber

Um Zink (OpenGL uber Vulkan) zu aktivieren, gehen Sie zu Einstellungen > Kompatibilitat > Zink-Modus.

---

## Lizenz

Dieses Projekt ist unter der **GNU General Public License v3.0** lizenziert.

**Namensnennung** — dieser Launcher basiert auf dem [mcpelauncher](https://github.com/minecraft-linux/mcpelauncher-manifest)-Projekt von ChristopherHX, MCMrARM und Mitwirkenden.

---

## Entwickler

**Ars-Byte**

---
<p align="center"><sub>Fur die Linux-Community entwickelt.</sub></p>
