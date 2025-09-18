# Alias liquid_s4.callbacks to the original top-level callbacks package
import importlib as _importlib
import sys as _sys
_sys.modules[__name__] = _importlib.import_module("callbacks")
