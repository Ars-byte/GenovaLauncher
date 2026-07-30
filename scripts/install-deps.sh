#!/bin/bash
# GenovaLauncher - Instalador de dependencias mcpelauncher
# Ejecutar: curl -sL https://raw.githubusercontent.com/Ars-byte/GenovaLauncher/main/scripts/install-deps.sh | bash
set -e

MCPE_URL="https://github.com/minecraft-linux/mcpelauncher-manifest/releases/download/v1.7.4/mcpelauncher-x86_64.tar.gz"
INSTALL_DIR="$HOME/.local/share/mcpelauncher/bin"

echo "=== Instalando dependencias de mcpelauncher ==="
echo ""

# Agregar ~/.local/bin al PATH si no está
if [ -d "$INSTALL_DIR" ] && [ -f "$INSTALL_DIR/mcpelauncher-client" ]; then
    echo "[!] Los binarios ya están instalados en $INSTALL_DIR"
else
    echo "[*] Descargando mcpelauncher v1.7.4..."
    mkdir -p "$INSTALL_DIR"
    TMP=$(mktemp -d)
    curl -sL "$MCPE_URL" -o "$TMP/mcpelauncher.tar.gz"
    tar -xzf "$TMP/mcpelauncher.tar.gz" -C "$TMP"
    cp "$TMP"/mcpelauncher-*/bin/* "$INSTALL_DIR/" 2>/dev/null || true
    rm -rf "$TMP"
    echo "[*] Binarios instalados en $INSTALL_DIR"
fi

# Agregar al PATH en ~/.bashrc
if ! grep -q "$INSTALL_DIR" "$HOME/.bashrc" 2>/dev/null; then
    echo "export PATH=\"$INSTALL_DIR:\$PATH\"" >> "$HOME/.bashrc"
    echo "[*] PATH actualizado en ~/.bashrc"
fi

export PATH="$INSTALL_DIR:$PATH"

echo ""
echo "=== Verificando binarios ==="
for BIN in mcpelauncher-client mcpelauncher-extract mcpelauncher-ui-qt mcpelauncher-webview playdl-signin-ui-qt gplaydl gplayver msa-daemon; do
    if [ -f "$INSTALL_DIR/$BIN" ]; then
        echo "  [OK] $BIN"
    else
        echo "  [--] $BIN (no encontrado, puede ser opcional)"
    fi
done

echo ""
echo "=== Instalación completa ==="
echo "Cerrá y volvé a abrir la terminal, o ejecutá:"
echo "  source ~/.bashrc"
echo "Después abrí GenovaLauncher y en Ajustes seleccioná modo 'Sistema'."