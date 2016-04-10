#!/usr/bin/env python3

from setuptools import setup, find_packages

NAME = "duka"
VERSION = '0.0.9'

setup(
    name=NAME,
    packages=find_packages(),
    install_requires=['aiohttp>=0.21.5'],
    version=VERSION,
    description='Dukascopy Bank SA historical data downloader',
    author='Giuseppe Pes',
    author_email='giuse88@gmail.com',
    url='https://github.com/giuse88/dukascopy-data-downloader',
    download_url='https://github.com/giuse88/dukascopy-data-downloader/tarball/' + VERSION,
    keywords=['dukascopy', 'forex', 'finance', 'historical data', 'price', 'currency'],
    entry_points={
        'console_scripts': [
            'duka = duka.main:main',
        ],
    },
    classifiers=[
        "Environment :: Console",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3 :: Only",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

