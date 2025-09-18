# Alias liquid_s4.tasks to the original top-level tasks package
import importlib as _importlib
import sys as _sys
_sys.modules[__name__] = _importlib.import_module("tasks")
