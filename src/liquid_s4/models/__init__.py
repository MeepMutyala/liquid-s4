# Alias liquid_s4.models to the original top-level models package
import importlib as _importlib
import sys as _sys
_sys.modules[__name__] = _importlib.import_module("models")
