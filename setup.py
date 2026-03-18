"""
Setup script for weave-generator
"""
from setuptools import setup
import sys

# Read the contents of README file
this_directory = sys.path[0]
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="weave-generator",
    version="1.0.2",
    author="Weave Generator Team",
    author_email="weave@example.com",
    description="纺织组织生成器 - 支持9种常见组织结构的Python库",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/weave-generator/weave-generator",
    package_dir={"": "src"},
    packages=["weave_generator"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
    ],
    python_requires=">=3.7",
    install_requires=[
        "numpy>=1.19.0",
    ],
    entry_points={
        "console_scripts": [
            "weave-gen=weave_generator.unified_interface:main",
        ],
    },
)
