from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(here, 'README.md'), 'r') as f:
        README = f.read()
except Exception:
    README = """\
This is a wonderful package. """

VERSION = '1.0.0' 

# Setting up
setup(
    name="my-minipack", 
    version=VERSION,
    description="How to create a package in python.",
    long_description=README,
    url="None",
    author="jle-corr",
    author_email="jle-corr@student.42.fr",
    license="MIT",
    packages=find_packages(),
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Students",
        "Topic :: Education",
        "Topic :: HowTo",
        "Topic :: Package",
        "License :: OSI Approved :: MIT",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
    ],
)
