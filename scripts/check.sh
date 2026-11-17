#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/verify_repository.py
python3 computations/verify_identities.py
python3 computations/verify_toric.py
