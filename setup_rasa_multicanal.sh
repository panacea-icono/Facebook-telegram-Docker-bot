#!/usr/bin/env bash
set -euo pipefail

# ============================
# Rasa Multicanal (Telegram + Facebook) — Scaffold
# ============================

mkdir -p actions data models
touch actions/__init__.py

# ---------- README ----------
cat > README.md <<'MD'
# Rasa Multicanal (Telegram + Facebook) — Docker Ready

Bot con **Rasa 3.x** que expone webhooks para **Telegram** y **Facebook Messenger**, preparado para **Docker** y **GitHub Codespaces**.

## Uso rápido
1) Copia `.env.example` → `.env` y completa tus tokens.  
2) Entrena:
```bash
docker compose run --rm rasa rasa train
