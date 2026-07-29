#!/bin/bash
set -e

echo "Setting up virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt pyinstaller

echo "Building executable..."
./venv/bin/pyinstaller --noconfirm --clean GenovaLauncher.spec

echo "Build complete!"
echo "Executable is located at: dist/GenovaLauncherMCPE"
