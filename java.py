import atexit
import builtins
import os
import types

import javabridge as jb


class JavaPackage(types.ModuleType):
    'An on-demand Java class loader.'

    def __getattribute__(self, attr):
        if attr.startswith('__'):
            return super().__getattribute__(attr)

        env = jb.get_env()
        if not env:
            jb.start_vm(class_path=class_path())
            atexit.register(jb.kill_vm)
            env = jb.get_env()

        class_name = self.__name__ + '.' + attr
        if env.find_class(class_name.replace('.', '/')):
            return jb.JClassWrapper(class_name)
        else:
            raise ModuleNotFoundError(class_name)


def class_path():
    'Read the $CLASSPATH environment variable.'
    return os.environ.get('CLASSPATH', '').split(os.pathsep) + jb.JARS


def new_import(name, *args, **kwargs):
    try:
        module = old_import(name, *args, **kwargs)
    except ModuleNotFoundError as e:
        module = JavaPackage(name)
        print(dir(module))
    finally:
        return module


old_import = builtins.__import__
builtins.__import__ = new_import
