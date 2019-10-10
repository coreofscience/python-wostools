================
Python WoS tools
================


.. image:: https://pyup.io/repos/github/coreofscience/python-wostools/shield.svg
     :target: https://pyup.io/repos/github/coreofscience/python-wostools/
     :alt: Updates

.. image:: https://img.shields.io/pypi/v/wostools.svg
    :target: https://pypi.python.org/pypi/wostools

.. image:: https://img.shields.io/travis/coreofscience/python-wostools.svg
    :target: https://travis-ci.org/coreofscience/python-wostools

.. image:: https://readthedocs.org/projects/python-wostools/badge/?version=latest
    :target: https://python-wostools.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://zenodo.org/badge/94160457.svg
   :target: https://zenodo.org/badge/latestdoi/94160457
   :alt: DOI: 10.5281/zenodo.1344261

Translates isi web of knowledge files into python objects.



* Free software: MIT license
* Documentation: https://python-wostools.readthedocs.io.


Quickstart
----------

Install the library by:

.. code-block:: bash

   $ pip install wostools

Say you want to grab the title of all the articles in an isi file, you can grab
`this example file`_.

.. code-block:: python

   >>> from wostools import CollectionLazy
   >>> collection = CollectionLazy('docs/examples/bit-pattern-savedrecs.txt')
   >>> for article in collection.articles:
   ...     print(article.TI)
   Structural control of ultra-fine CoPt nanodot arrays via electrodeposition process
   Porphyrin-based Pt/Pd-containing metallopolymers: Synthesis, characterization, optical property and potential application in bioimaging
   Syntheses and Controllable Self-Assembly of Luminescence Platinum(II) Plane-Coil Diblock Copolymers
   # ...

Never fear wostools cli is here. To help you do some common tasks right from
your terminal.

.. code-block:: bash

   $ wostools --help
   $ # To build a citation graph full with properties
   $ wostools citation-graph docs/examples/bit-pattern-savedrecs.txt output.graphml

Features
--------

* Just parses an isi web of knowledge file and produces a native python object.
* Through the :code:`CollectionLazy` object it can do this using the minimum
  ammount of memory it can possibly do.
* It has a cli to generate graphs and analyze stuff for you :smile:

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _`this example file`: docs/examples/bit-pattern-savedrecs.txt
