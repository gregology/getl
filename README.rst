==================
Google Takeout ETL
==================

.. image:: https://badge.fury.io/py/getl.svg
    :target: https://badge.fury.io/py/getl

.. image:: http://img.shields.io/badge/license-MIT-yellow.svg?style=flat
    :target: https://github.com/gregology/getl/blob/master/LICENSE

.. image:: https://img.shields.io/badge/contact-Gregology-blue.svg?style=flat
    :target: http://gregology.net/contact/



Overview
--------

Extracts, transforms, and loads your data from `Google Takeout <https://takeout.google.com/settings/takeout>`_ into an SQLite DB.

Installation
------------

``getl`` is available on PyPI

http://pypi.python.org/pypi/getl

Install via ``pip``
::

    $ pip install getl

Or via ``easy_install``
::

    $ easy_install getl

Or directly from ``getl``'s `git repo <https://github.com/gregology/getl>`
::

    $ git clone git://github.com/gregology/getl.git
    $ cd getl
    $ python setup.py install

Basic usage
-----------

Download your data with `Google Takeout <https://takeout.google.com/settings/takeout>`_ using the format JSON and unzip the file.

.. image:: https://user-images.githubusercontent.com/1595448/46498508-a4bea680-c7eb-11e8-8ff7-b4a7870193ee.png
         :width: 80%

Currently only Location History works but I will implement more extractors shortly.

::

    >>> from getl import Getl
    >>> getl = Getl('path/to/unzipped/google/takeout/data')
    >>> getl.load_location_history()
    >>> getl.sql('SELECT COUNT(*) FROM locations')[0][0]
    5000
    >>> getl.sql('SELECT timestamp FROM locations LIMIT 5;')
    [('2018-07-27 14:04:24',), ('2018-07-23 11:34:12',), ('2018-07-17 09:47:19',), ('2018-07-13 23:56:44',), ('2018-07-12 09:54:13',)]
    >>> getl.save('foo.db') # Saves SQLite db to disk


Running Test
------------
::

    $ python tests/tests.py

Python compatibility
--------------------

Requires Python 3.0 or greater
