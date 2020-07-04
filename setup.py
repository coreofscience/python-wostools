#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("HISTORY.md") as history_file:
    history = history_file.read()

requirements = ["Click>=7.0"]

setup_requirements = ["pytest-runner"]


test_requirements = ["pytest", "pytest-bdd", 'dataclasses; python_version<"3.7"']

setup(
    author="Core of Science",
    author_email="dev@coreofscience.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    entry_points={"console_scripts": ["wostools=wostools.cli:main"]},
    description="Translates isi web of knowledge files into python objects.",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="wostools",
    name="wostools",
    packages=find_packages(include=["wostools", "wostools.*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/coreofscience/python-wostools",
    version="1.1.0",
    zip_safe=False,
    long_description_content_type="text/markdown",
)
