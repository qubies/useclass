from setuptools import setup, find_packages
from setuptools.command.install import install
from subprocess import check_call

setup(
    name="useclass",
    version="1.0.1",
    include_package_data=True,
    url="https://github.com/qubies/use_class",
    author="Tobias Renwick",
    author_email="tobias@renwick.tech",
    description="a wrapper for the universal sentence encoder",
    packages=find_packages(),
    install_requires=[],
)

