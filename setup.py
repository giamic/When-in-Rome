#!/usr/bin/env python

from distutils.core import setup
from pathlib import Path

from setuptools import find_packages


def read_version() -> str:
    """
    This script reads the information inside Code/__init__.py without
     importing the package, which is not allowed inside the setup.py file
    """
    version = None

    with open(Path(__file__).parent / "Code" / "__init__.py", "r") as f:
        lines = f.readlines()

    for line in lines:
        if line.startswith("__version__"):
            version = line.split('"')[1]
    if version is None:
        raise RuntimeError("Can't read package version from file Code/__init__.py")
    return version


setup(
    name="When in Rome",
    version=read_version(),
    description="",
    author="Mark Gotham",
    author_email="",
    url="https://github.com/MarkGotham/When-in-Rome/",
    python_requires=">=3.7",
    install_requires=["music21", "numpy"],
    packages=find_packages(),
)
