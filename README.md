# Python WoS tools

![Python package](https://github.com/coreofscience/python-wostools/workflows/Python%20package/badge.svg)
[![image](https://img.shields.io/pypi/v/wostools.svg)](https://pypi.python.org/pypi/wostools)
[![DOI: 10.5281/zenodo.1344261](https://zenodo.org/badge/94160457.svg)](https://zenodo.org/badge/latestdoi/94160457)

Translates ISI Web of Knowledge files into python objects.

## Quickstart

Install the library by:

```bash
$ pip install wostools
```

Say you want to grab the title of all the articles in an ISI file, you
can grab [this example file](docs/examples/bit-pattern-savedrecs.txt).

```python
>>> from wostools import Cached
>>> collection = Cached.from_filenames('docs/examples/bit-pattern-savedrecs.txt')
>>> for article in collection:
...     print(article.title)
In situ grazing incidence small-angle X-ray scattering study of solvent vapor annealing in lamellae-forming block copolymer thin films: Trade-off of defects in deswelling
Structural control of ultra-fine CoPt nanodot arrays via electrodeposition process
Porphyrin-based Pt/Pd-containing metallopolymers: Synthesis, characterization, optical property and potential application in bioimaging
Syntheses and Controllable Self-Assembly of Luminescence Platinum(II) Plane-Coil Diblock Copolymers
# ...
```

Never fear wostools cli is here. To help you do some common tasks right
from your terminal.

```bash
$ wostools --help
$ # To extract all the properties in a json file
$ wostools to-json docs/examples/bit-pattern-savedrecs.txt --output=document.json
```

## Features

- Free software: MIT license
- Parses an ISI Web of Knowledge file and produces a native python object.
- Parses RIS scopus files and produces a native python object.
- Merges ISI and RIS files into enriched collections.
- It has a cli to extract documents and citation pairs for you :smile:

## Credits

This package was created with
[Cookiecutter](https://github.com/audreyr/cookiecutter) and the
[audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)
project template.

Development of this package is supported by [Core of Science](https://coreofscience.com).