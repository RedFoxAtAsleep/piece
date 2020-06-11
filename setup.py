# -*- coding: utf-8 -*-

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="piece", # Replace with your own username
    version="0.0.1",
    author="3941",
    author_email="bbxxone@qq.com",
    description="Useful Code Piece.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RedFoxAtAsleep/piece",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)
