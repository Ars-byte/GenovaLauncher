#!/bin/bash
# Package GenovaLauncher into .deb, .xbps, and .AppImage
set -euo pipefail

VERSION="1.3.1"
ARCH_DEB="amd64"
ARCH_XBPS="x86_64"
ROOT="$(cd "$(dirname "$0")" && pwd)"
DIST="$ROOT/dist/GenovaLauncherMCPE"
OUT="$ROOT/packages"
mkdir -p "$OUT"

echo "=== Building GenovaLauncher $VERSION packages ==="

# ──────────────────────────────────────────────
# 1. .deb
# ──────────────────────────────────────────────
echo ""
echo "--- Creating .deb ---"

DEB_DIR="$OUT/genovalauncher_${VERSION}_${ARCH_DEB}"
rm -rf "$DEB_DIR"

# Binary
mkdir -p "$DEB_DIR/usr/bin"
cat > "$DEB_DIR/usr/bin/genovalauncher" << 'SCRIPT'
#!/bin/bash
exec /usr/share/genovalauncher/GenovaLauncherMCPE "$@"
SCRIPT
chmod 755 "$DEB_DIR/usr/bin/genovalauncher"

# Main app files
mkdir -p "$DEB_DIR/usr/share/genovalauncher"
cp -a "$DIST"/* "$DEB_DIR/usr/share/genovalauncher/"

# .desktop
mkdir -p "$DEB_DIR/usr/share/applications"
cat > "$DEB_DIR/usr/share/applications/genovalauncher.desktop" << EOF
[Desktop Entry]
Name=GenovaLauncher
Comment=Minecraft Bedrock Launcher for Linux
Exec=genovalauncher
Icon=genovalauncher
Terminal=false
Type=Application
Categories=Game;
EOF

# Icon
mkdir -p "$DEB_DIR/usr/share/icons/hicolor/256x256/apps"
cp "$ROOT/icon.png" "$DEB_DIR/usr/share/icons/hicolor/256x256/apps/genovalauncher.png"

# Control file
mkdir -p "$DEB_DIR/DEBIAN"
cat > "$DEB_DIR/DEBIAN/control" << EOF
Package: genovalauncher
Version: ${VERSION}
Section: games
Priority: optional
Architecture: ${ARCH_DEB}
Maintainer: Ars-Byte <arsbyte@github>
Description: Unofficial Minecraft Bedrock Launcher for Linux
 GenovaLauncher is an unofficial launcher for Minecraft Bedrock
 Edition on Linux, powered by the mcpelauncher project.
Homepage: https://github.com/Ars-byte/GenovaLauncher
EOF

# Post-install: update icon cache
cat > "$DEB_DIR/DEBIAN/postinst" << 'SCRIPT'
#!/bin/sh
set -e
if command -v gtk-update-icon-cache >/dev/null 2>&1; then
    gtk-update-icon-cache -q /usr/share/icons/hicolor 2>/dev/null || true
fi
exit 0
SCRIPT
chmod 755 "$DEB_DIR/DEBIAN/postinst"

# Build .deb manually (ar + tar)
cd "$OUT"
# debian-binary
echo "2.0" > debian-binary
# control.tar.gz
tar -czf control.tar.gz --owner=0 --group=0 \
    -C "$DEB_DIR/DEBIAN" .
# data.tar.gz
tar -czf data.tar.gz --owner=0 --group=0 \
    -C "$DEB_DIR" --exclude=DEBIAN usr
# Assemble .deb (ar archive)
ar -rcs "genovalauncher_${VERSION}_${ARCH_DEB}.deb" debian-binary control.tar.gz data.tar.gz
rm -f debian-binary control.tar.gz data.tar.gz
echo "  -> genovalauncher_${VERSION}_${ARCH_DEB}.deb"
cd "$ROOT"
echo "  -> genovalauncher_${VERSION}_${ARCH_DEB}.deb"

# ──────────────────────────────────────────────
# 2. .xbps (Void Linux)
# ──────────────────────────────────────────────
echo ""
echo "--- Creating .xbps ---"

XBPS_DIR="$OUT/xbps-root"
rm -rf "$XBPS_DIR"
mkdir -p "$XBPS_DIR/usr/bin"
mkdir -p "$XBPS_DIR/usr/share/genovalauncher"
mkdir -p "$XBPS_DIR/usr/share/applications"
mkdir -p "$XBPS_DIR/usr/share/icons/hicolor/256x256/apps"

# Same content as deb (without DEBIAN metadata)
cp "$DEB_DIR/usr/bin/genovalauncher" "$XBPS_DIR/usr/bin/"
cp -a "$DIST"/* "$XBPS_DIR/usr/share/genovalauncher/"
cp "$DEB_DIR/usr/share/applications/genovalauncher.desktop" "$XBPS_DIR/usr/share/applications/"
cp "$ROOT/icon.png" "$XBPS_DIR/usr/share/icons/hicolor/256x256/apps/genovalauncher.png"

# Create xbps package (output goes to cwd, named by arch)
cd "$OUT"
xbps-create \
    -A "x86_64" \
    -n "genovalauncher-${VERSION}_1" \
    --maintainer "Ars-Byte <arsbyte@github>" \
    --homepage "https://github.com/Ars-byte/GenovaLauncher" \
    --desc "Unofficial Minecraft Bedrock Launcher for Linux" \
    "$XBPS_DIR"
xbps-rindex -a "genovalauncher-${VERSION}_1.x86_64.xbps" 2>/dev/null || true
echo "  -> genovalauncher-${VERSION}_1.x86_64.xbps"
cd "$ROOT"

# ──────────────────────────────────────────────
# 3. .AppImage
# ──────────────────────────────────────────────
echo ""
echo "--- Creating AppImage ---"

APPDIR="$OUT/GenovaLauncher.AppDir"
rm -rf "$APPDIR"
mkdir -p "$APPDIR/usr"

# AppRun
cat > "$APPDIR/AppRun" << 'SCRIPT'
#!/bin/bash
APPDIR="$(dirname "$(readlink -f "$0")")"
export PATH="${APPDIR}/usr/bin:${PATH}"
exec "${APPDIR}/usr/bin/genovalauncher" "$@"
SCRIPT
chmod 755 "$APPDIR/AppRun"

# Binary
mkdir -p "$APPDIR/usr/bin"
cat > "$APPDIR/usr/bin/genovalauncher" << 'SCRIPT'
#!/bin/bash
APPDIR="$(dirname "$(dirname "$(readlink -f "$0")")")"
exec "${APPDIR}/share/GenovaLauncherMCPE" "$@"
SCRIPT
chmod 755 "$APPDIR/usr/bin/genovalauncher"

# Share (the actual PyInstaller build)
mkdir -p "$APPDIR/share"
cp -a "$DIST" "$APPDIR/share/GenovaLauncherMCPE"

# .desktop
cat > "$APPDIR/genovalauncher.desktop" << EOF
[Desktop Entry]
Name=GenovaLauncher
Comment=Minecraft Bedrock Launcher for Linux
Exec=genovalauncher
Icon=genovalauncher
Terminal=false
Type=Application
Categories=Game;
StartupWMClass=GenovaLauncherMCPE
EOF

cp "$ROOT/icon.png" "$APPDIR/genovalauncher.png"

# Build AppImage with appimagetool
/tmp/appimagetool --comp gzip "$APPDIR" "$OUT/GenovaLauncher-${VERSION}-x86_64.AppImage" 2>&1 | grep -v "^$"
echo "  -> GenovaLauncher-${VERSION}-x86_64.AppImage"

# ──────────────────────────────────────────────
# Done
# ──────────────────────────────────────────────
echo ""
echo "=== Packages ready in $OUT ==="
ls -lh "$OUT"/*.{deb,xbps,AppImage} 2>/dev/null || true
