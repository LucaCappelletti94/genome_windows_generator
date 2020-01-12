import os
import re
# To use a consistent encoding
from codecs import open as copen

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the relevant file
with copen(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


def read(*parts):
    with copen(os.path.join(here, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


__version__ = find_version("windows_generator", "__version__.py")

test_deps =[
    "validate_version_code",
    "codacy-coverage",
    "pytest-cov",
    "coveralls",
    "pytest"
]

extras = {
    'test': test_deps,
}

setup(
    name='windows_generator',
    version=__version__,
    description="![](https://github.com/zommiommy/windows_generator/workflows/Python%20package/badge.svg)",
    long_description=long_description,
    url="https://github.com/zommiommy/windows_generator",
    author="Tommaso Fontana",
    author_email="tommaso.fontana.96@gmail.com",
    # Choose your license
    license='MIT',
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    tests_require=test_deps,
    # Add here the package dependencies
    install_requires=[
        "compress-pickle",
        "numpy",
        "pandas",
        "tqdm",
        "ucsc-genomes-downloader"
        ],
    extras_require=extras,
)
