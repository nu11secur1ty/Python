
Installation
------------

The easiest way to install ``num2words`` is to use pip::

    pip install num2words

Otherwise, you can download the source package and then execute::

    python setup.py install

The test suite in this library is new, so it's rather thin, but it can be run with::

    python setup.py test

To run the full CI test suite which includes linting and multiple python environments::

    pip install tox
    tox

Usage
-----
Command line::

    $ num2words 10001
    ten thousand and one
    $ num2words 24,120.10
    twenty-four thousand, one hundred and twenty point one
    $ num2words 24,120.10 -l es
    veinticuatro mil ciento veinte punto uno
    $num2words 2.14 -l es --to currency
    dos euros con catorce centimos

In code there's only one function to use::

    >>> from num2words import num2words
    >>> num2words(42)
    forty-two
    >>> num2words(42, to='ordinal')
    forty-second
    >>> num2words(42, lang='fr')
    quarante-deux

Besides the numerical argument, there are two main optional arguments.

**to:** The converter to use. Supported values are:

* ``cardinal`` (default)
* ``ordinal``
* ``ordinal_num``
* ``year``
* ``currency``

**lang:** The language in which to convert the number. Supported values are:

* ``en`` (English, default)
* ``ar`` (Arabic)
* ``cz`` (Czech)
* ``de`` (German)
* ``dk`` (Danish)
* ``en_GB`` (English - Great Britain)
* ``en_IN`` (English - India)
* ``es`` (Spanish)
* ``es_CO`` (Spanish - Colombia)
* ``es_VE`` (Spanish - Venezuela)
* ``eu`` (EURO)
* ``fi`` (Finnish)
* ``fr`` (French)
* ``fr_CH`` (French - Switzerland)
* ``fr_BE`` (French - Belgium)
* ``fr_DZ`` (French - Algeria)
* ``he`` (Hebrew)
* ``id`` (Indonesian)
* ``it`` (Italian)
* ``ja`` (Japanese)
* ``kn`` (Kannada)
* ``ko`` (Korean)
* ``kz`` (Kazakh)
* ``lt`` (Lithuanian)
* ``lv`` (Latvian)
* ``no`` (Norwegian)
* ``pl`` (Polish)
* ``pt`` (Portuguese)
* ``pt_BR`` (Portuguese - Brazilian)
* ``sl`` (Slovene)
* ``sr`` (Serbian)
* ``ro`` (Romanian)
* ``ru`` (Russian)
* ``te`` (Telugu)
* ``tr`` (Turkish) - Without manual script
* ``th`` (Thai)
* ``vi`` (Vietnamese)
* ``nl`` (Dutch)
* ``uk`` (Ukrainian)

You can supply values like ``fr_FR``; if the country doesn't exist but the
language does, the code will fall back to the base language (i.e. ``fr``). If
you supply an unsupported language, ``NotImplementedError`` is raised.
Therefore, if you want to call ``num2words`` with a fallback, you can do::

    try:
        return num2words(42, lang=mylang)
    except NotImplementedError:
        return num2words(42, lang='en')

Additionally, some converters and languages support other optional arguments
that are needed to make the converter useful in practice.

Wiki
----
For additional information on some localization please check the Wiki_.
And feel free to propose wiki enhancement.

.. _Wiki: https://github.com/savoirfairelinux/num2words/wiki

# Module
`https://pypi.org/project/num2words/`

# Manual script: 
![Link](https://github.com/nu11secur1ty/Python/blob/master/Python3/nums_string/USAGE.md)
