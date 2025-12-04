from setuptools import setup, find_packages

setup(
    name="pyrmifeem",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'pydicom>=2.3.0',
        'numpy>=1.21.0'
    ],
)

