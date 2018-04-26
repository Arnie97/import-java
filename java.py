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
            env = jb.get_env()

        class_name = self.__name__ + '.' + attr
        if env.find_class(class_name.replace('.', '/')):
            return jb.JClassWrapper(class_name)
        else:
            raise ModuleNotFoundError(class_name)


def class_path():
    'Read the $CLASSPATH environment variable.'
    return os.environ.get('CLASSPATH', '').split(os.pathsep) + jb.JARS


class Context():
    'Patch or recover the __import__ function.'

    def new_import(self, name, *args, **kwargs):
        try:
            module = self.old_import(name, *args, **kwargs)
        except ModuleNotFoundError as e:
            module = JavaPackage(name)
        finally:
            return module

    def __enter__(self):
        self.old_import = builtins.__import__
        builtins.__import__ = self.new_import

    def __exit__(self, *_):
        builtins.__import__ = self.old_import
