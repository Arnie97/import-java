import builtins
import os
import types


class JavaPackage(types.ModuleType):
    'An on-demand Java class loader.'

    def __getattribute__(self, attr):
        if attr.startswith('__'):
            return super().__getattribute__(attr)

        class_name = self.__name__ + '.' + attr
        try:
            return autoclass(class_name)
        except JavaException:
            raise ModuleNotFoundError(class_name)


def class_path():
    'Read the $CLASSPATH environment variable.'
    return os.environ.get('CLASSPATH', '').split(os.pathsep)


class Context():
    'Patch or recover the __import__ function.'

    def new_import(self, name, *args, **kwargs):
        try:
            module = self.old_import(name, *args, **kwargs)
        except ModuleNotFoundError as e:
            # shortcut for the default package
            if name == '_':
                name = 'java.lang'
            module = JavaPackage(name)
        finally:
            return module

    def __enter__(self):
        self.old_import = builtins.__import__
        builtins.__import__ = self.new_import

    def __exit__(self, *_):
        builtins.__import__ = self.old_import


try:
    from jnius import autoclass, JavaException
except ModuleNotFoundError:
    from javabridge import JClassWrapper as autoclass, JavaException

    import javabridge as jb
    if not jb.get_env():
        jb.start_vm(class_path=class_path() + jb.JARS)
