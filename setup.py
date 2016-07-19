import os
from setuptools import setup


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


setup(
    name='djangopatchy',
    description='Useful django patch for luojilab team',
    author='Fu Jian',
    author_email='fujian@luojilab.com',
    packages=get_packages('patchy'),
    zip_safe=False
)
