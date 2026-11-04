#!/usr/bin/env bash
# Enlaza el cerebro a ~/.claude para usar memoria, skills y agentes en TODOS los proyectos de este equipo.
# Uso: ./scripts/instalar-local.sh   (desde tu clon del repo)
set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
DEST="${HOME}/.claude"
mkdir -p "$DEST"

enlazar() {
  local origen="$1" destino="$2"
  if [ -e "$destino" ] && [ ! -L "$destino" ]; then
    mv "$destino" "${destino}.respaldo-$(date +%Y%m%d%H%M%S)"
    echo "Respaldo creado de $destino"
  fi
  ln -sfn "$origen" "$destino"
  echo "Enlazado: $destino -> $origen"
}

enlazar "$REPO/CLAUDE.md"        "$DEST/CLAUDE.md"
enlazar "$REPO/memoria"          "$DEST/memoria"
enlazar "$REPO/.claude/skills"   "$DEST/skills"
enlazar "$REPO/.claude/agents"   "$DEST/agents"

echo "Listo. Ejecuta 'git pull' en $REPO para sincronizar cambios hechos desde otros dispositivos."
