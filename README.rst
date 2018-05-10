================
Python WoS tools
================


.. image:: https://img.shields.io/pypi/v/wostools.svg
        :target: https://pypi.python.org/pypi/wostools

.. image:: https://img.shields.io/travis/coreofscience/wostools.svg
        :target: https://travis-ci.org/coreofscience/wostools

.. image:: https://readthedocs.org/projects/wostools/badge/?version=latest
        :target: https://wostools.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


Translates isi web of knowledge files into python objects.

* Free software: MIT license
* Documentation: https://wostools.readthedocs.io.


Quickstart
----------

Say you want to grab the title of all the articles in an isi file, you can grab
`this example file`_.

    >>> from wostools import CollectionLazy
    >>> collection = CollectionLazy('docs/examples/bit-pattern-savedrecs.txt')
    >>> for article in collection.articles:
    ...     print(article.TI)
    # ['Structural control of ultra-fine CoPt nanodot arrays via', 'electrodeposition process']
    # ['Porphyrin-based Pt/Pd-containing metallopolymers: Synthesis,', 'characterization, optical property and potential application in', 'bioimaging']
    # ['Syntheses and Controllable Self-Assembly of Luminescence Platinum(II)', 'Plane-Coil Diblock Copolymers']
    # ...

Features
--------

* Just parses an isi web of knowledge file and produces a native python object.
* Through the :code:`CollectionLazy` object it can do this using the minimum
  ammount of memory it can possibly do.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _`this example file`: docs/examples/bit-pattern-savedrecs.txt
