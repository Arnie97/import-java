from os import path
from setuptools import setup
from pkg_resources import get_distribution, DistributionNotFound


def get_dist(pkg_name, default=None):
    try:
        return get_distribution(pkg_name)
    except DistributionNotFound:
        return default


here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    readme = f.read()

setup(
    name='import-java',
    use_scm_version=True,
    description='Import Java packages seamlessly into CPython',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/Arnie97/import-java',
    author='Arnie97',
    author_email='Arnie97@gmail.com',
    license='MIT',
    py_modules=['java'],
    python_requires='>=3.0',
    install_requires=['javabridge' if get_dist('javabridge') else 'pyjnius'],
    setup_requires=['pytest-runner', 'setuptools_scm'],
    tests_require=['pytest-cov', 'pytest-flake8'],
    zip_safe=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Java Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Java',
    ],
)
