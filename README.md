# import-java
[![Build Status](https://travis-ci.org/Arnie97/import-java.svg)](https://travis-ci.org/Arnie97/import-java)
[![Code Coverage](https://codecov.io/gh/Arnie97/import-java/branch/master/graph/badge.svg)](https://codecov.io/gh/Arnie97/import-java)
[![PyPI Version](https://img.shields.io/pypi/v/import-java.svg)](https://pypi.org/project/import-java)
[![Python Compatibility](https://img.shields.io/pypi/pyversions/import-java.svg)](https://pypi.org/project/import-java)
[![License](https://img.shields.io/pypi/l/import-java.svg)](LICENSE)

Import your Java packages seamlessly into CPython.

## Quick Start
We'll create a temporary file in Java and then read it in Python to illustrate the usage:

```python
>>> import java
>>> with java:
...     from java.lang import String
...     from java.nio.file import Files
...
>>> temp_path = Files.createTempFile('sample', '.tmp')
>>> sample_text = String('Greetings from Java')
>>> Files.write(temp_path, sample_text.getBytes())
<java.nio.file.Path at 0x... jclass=java/nio/file/Path jself=...>

>>> with open(temp_path.toString()) as f:
...     print(repr(f.read()))
...
'Greetings from Java'

```

You can also use `_` as a short alias for `java.lang`:

```python
>>> with java:
...     from _ import System
...
>>> System.getProperties().get('java.specification.version')
'1.8'

```

Wildcard imports (such as `from java.util import *`) are not supported yet.

## Dependencies
Either [PyJNIus](https://github.com/kivy/pyjnius) or [JavaBridge](https://github.com/LeeKamentsky/python-javabridge). PyJNIus is preferred, as [JavaBridge cannot disambiguate overloaded methods with the same number of parameters](https://github.com/LeeKamentsky/python-javabridge/issues/55).

## Installation
`$ pip install import-java`

## License
MIT.

## See also
* [pythonnet](https://github.com/pythonnet/pythonnet) - Import .NET CLR modules
* [hack-py-import](https://github.com/iblis17/hack-py-import) - Import your C libraries
