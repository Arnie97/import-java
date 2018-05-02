import pytest
from _pytest.doctest import DoctestItem


try:
    from javabridge import kill_vm

except ImportError:
    pass

else:
    def pytest_runtest_setup(item):
        'Doctest failures expected due to a different repr.'
        if isinstance(item, DoctestItem):
            mark = dict(xfail=pytest.mark.xfail(run=True))
            item.keywords._markers.update(mark)

    def pytest_unconfigure(config):
        'Shut down the JVM instance after tests.'
        kill_vm()
