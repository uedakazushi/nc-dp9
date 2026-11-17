#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/verify_repository.py
python3 computations/verify_normalized_index.py
python3 computations/verify_del_pezzo_roots.py
python3 computations/verify_identities.py
python3 computations/verify_toric.py
python3 computations/verify_root_deformations.py
python3 computations/verify_artin_roots.py
