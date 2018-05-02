def pytest_unconfigure(config):
    'Shut down the JVM instance after tests.'
    try:
        from javabridge import kill_vm
    except ImportError:
        pass
    else:
        kill_vm()
