"""Shared test helpers for stage-signals-x-quotes eval checks."""

import importlib.util
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[5]
SCRIPT_PATH = REPO_ROOT / ".agents/skills/stage-signals-x-quotes/scripts/stage_signals_x_quotes.py"


def load_script():
    spec = importlib.util.spec_from_file_location("stage_signals_x_quotes", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    return module
