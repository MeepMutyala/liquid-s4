# Make top-level packages importable under the liquid_s4 namespace without moving files.
# We alias existing top-level packages (models, tasks, utils, callbacks, dataloaders)
# by creating package stubs that point their __path__ to the original locations.
# This avoids importing heavy dependencies at import time (e.g., torch).

import sys as _sys
import types as _types
import importlib.util as _util

def _alias_pkg(_alias: str, _target: str):
    spec = _util.find_spec(_target)
    if spec is None or getattr(spec, "submodule_search_locations", None) is None:
        return
    mod = _types.ModuleType(_alias)
    # Point to the original package directory so submodule imports resolve
    mod.__path__ = list(spec.submodule_search_locations)
    mod.__package__ = _alias
    _sys.modules[_alias] = mod

for _name in ("models", "tasks", "utils", "callbacks", "dataloaders"):
    _alias_pkg(__name__ + "." + _name, _name)
