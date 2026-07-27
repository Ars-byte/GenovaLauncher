#!/bin/bash
# Sunshine Launcher — verbose runner.
# Habilita logs detallados del flujo Google Play (login/exchange/download).
# Variables que afecta el código:
#   SUNSHINE_DEBUG=1            → activa prints de src/core/app_logic.py
#   PYTHONUNBUFFERED=1         → flush inmediato (stdout)
#   PYTHONFAULTHANDLER=1       → tracebacks completos en crash
# Logs guardados en logs/sunshine-YYYYmmdd-HHMMSS.log (tee a la terminal).

cd "$(dirname "$0")"
source venv/bin/activate
export PYTHONPATH="$PYTHONPATH:$(pwd)"
export PYTHONUNBUFFERED=1
export PYTHONFAULTHANDLER=1
export SUNSHINE_DEBUG="${SUNSHINE_DEBUG:-1}"
# Bundled libs (libzip.so.5 for mcpelauncher-extract, etc.)
export LD_LIBRARY_PATH="$(pwd)/bin/lib:${LD_LIBRARY_PATH}"

mkdir -p logs
LOG="logs/sunshine-$(date +%Y%m%d-%H%M%S).log"
echo "[run.sh] SUNSHINE_DEBUG=$SUNSHINE_DEBUG  log=$LOG"
echo "[run.sh] PWD=$(pwd)"
echo "[run.sh] python=$(python3 -V)  bin/gplaydl=$(ls -l bin/gplaydl 2>&1 | awk '{print $5,$NF}')"
echo "[run.sh] -- launching --"

set -o pipefail
python3 -u src/main.py "$@" 2>&1 | tee "$LOG"
exit ${PIPESTATUS[0]}
