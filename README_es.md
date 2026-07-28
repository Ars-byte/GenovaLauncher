# PYmc


> Website: [ars-byte.github.io/sunshine-website](https://ars-byte.github.io/sunshine-website/)

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![PySide6](https://img.shields.io/badge/UI-PySide6-green?style=flat-square&logo=qt&logoColor=white)](https://www.qt.io/qt-for-python)
[![Platform](https://img.shields.io/badge/Platform-Linux-FCC624?style=flat-square&logo=linux&logoColor=black)](https://www.kernel.org/)
[![License](https://img.shields.io/badge/License-GPL%20v3-red?style=flat-square)](LICENSE)

Launcher grafico moderno para **Minecraft: Bedrock Edition** en Linux, construido con PySide6 (Qt6) y basado en el proyecto [mcpelauncher](https://github.com/minecraft-linux/mcpelauncher-manifest).

---

## Caracteristicas

- **Gestion de versiones** — instala, cambia y juega multiples versiones de Minecraft Bedrock desde APK o Google Play
- **Integracion con Google Play** — descarga versiones directamente desde tu biblioteca de Play Store
- **Gestor de recursos** — administra paquetes de recursos, comportamientos, skins y mundos desde una sola interfaz
- **Soporte de mods** — explora e instala mods desde el repositorio oficial mcpelauncher-moddb
- **Perfiles independientes** — cada perfil mantiene sus propios mundos, configuraciones y datos mediante symlinks
- **Optimizaciones Nvidia** — soporte para Nvidia Prime y Zink (OpenGL sobre Vulkan)
- **Migracion de datos** — importa mundos, versiones y recursos desde otros launchers
- **Multi-idioma** — ingles, espanol, aleman, frances, italiano, portugues, catalan y japones

---

## Requisitos

- **Linux** x86_64
- **Python** 3.10 o superior
- **OpenGL ES 3.0** o superior (para versiones modernas de Minecraft Bedrock)
- **Binarios mcpelauncher** — descarga los binarios precompilados desde [mcpelauncher](https://github.com/minecraft-linux/mcpelauncher-manifest/releases)

### Dependencias del sistema

```bash
# Void Linux
doas xbps-install qt6-base qt6-webengine qt6-declarative qt6-webchannel qt6-position libzip unzip zenity

# Debian/Ubuntu
sudo apt install qt6-base qt6-webengine qt6-declarative qt6-webchannel libzip unzip zenity

# Arch
# NixOS (flake)
# Agrega a tu flake.nix en inputs:
#   pymc.url = "github:Ars-byte/Sunshine-launcher";
sudo pacman -S qt6-base qt6-webengine qt6-declarative qt6-webchannel libzip unzip zenity
```

---

## Instalacion

### Void Linux (paquete xbps)

```bash
xbps-rindex -a pymc-1.0.0_1.x86_64.xbps
doas xbps-install -R $PWD pymc
pymc
```

### Desde el release portable

1. Descarga el ultimo `PYmc-v*.tar.gz` de [Releases](https://github.com/Ars-byte/Sunshine-launcher/releases)
2. Extrae en cualquier directorio
3. Ejecuta:

```bash
./PYmc.sh
```

### Desde el codigo fuente

```bash
git clone https://github.com/Ars-byte/Sunshine-launcher.git
cd Sunshine-launcher
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
./run.sh
```

---

## Rendimiento

PYmc aplica automaticamente optimizaciones para mejorar el rendimiento del juego:

- `mesa_glthread=true` — despacho GL multihilo para GPUs Intel/AMD
- Cache de shaders persistente (`~/.cache/sunshine-shaders/`)
- `MESA_NO_ERROR=1` — omite verificacion de errores GL en produccion
- `ANV_SPARSE=1` — memoria dispersa Vulkan para el driver Intel ANV

Para activar Zink (OpenGL sobre Vulkan, recomendado en GPUs modernas), ve a Ajustes > Compatibilidad > Modo Zink.

---

## Licencia

Este proyecto esta licenciado bajo **GNU General Public License v3.0**.

**Atribucion** — este launcher se basa en el proyecto [mcpelauncher](https://github.com/minecraft-linux/mcpelauncher-manifest) de ChristopherHX, MCMrARM y colaboradores.

---

## Desarrollador

**Ars-Byte**

---
<p align="center"><sub>Creado para la comunidad Linux.</sub></p>
