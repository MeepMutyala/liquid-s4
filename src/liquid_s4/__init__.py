# Make top-level packages importable under the liquid_s4 namespace without moving files.
# We alias existing top-level packages (models, tasks, utils, callbacks, dataloaders)
# so imports like `from liquid_s4.models.sequence.model import SequenceModel` work.
import importlib as _importlib
import sys as _sys

for _name in ("models", "tasks", "utils", "callbacks", "dataloaders"):
    try:
        _mod = _importlib.import_module(_name)
        _sys.modules[__name__ + "." + _name] = _mod
    except Exception:
        # It's okay if some optional subpackages don't exist
        pass
