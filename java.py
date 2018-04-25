import builtins
import pprint
import types

import javabridge as jb


def new_import(name, *args, **kwargs):
    try:
        module = old_import(name, *args, **kwargs)
    except ModuleNotFoundError as e:
        pprint.pprint(args)
        module = types.ModuleType(name)
        module.__getattr__ = lambda cls: \
            jb.JClassWrapper(self.__name__ + '.' + attr)
    finally:
        return module


old_import = builtins.__import__
builtins.__import__ = new_import
