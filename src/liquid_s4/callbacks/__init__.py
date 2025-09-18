# Package stub to map liquid_s4.callbacks to the original 'callbacks' package path
import importlib.util as _util
import sys as _sys
import types as _types
_spec = _util.find_spec("callbacks")
if _spec and getattr(_spec, "submodule_search_locations", None):
    _pkg = _types.ModuleType(__name__)
    _pkg.__path__ = list(_spec.submodule_search_locations)
    _pkg.__package__ = __name__
    _sys.modules[__name__] = _pkg
