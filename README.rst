virtualenv-pythonw-osx
======================

In Mac OSX, many GUI-based Python apps run inside a virtualenv
only work correctly when the ``pythonw`` executable is located
within an app bundle.

This tool fixes virtualenvs based on Framework style Python builds.
It does so by making sure both ``python`` and ``pythonw`` get
compiled like app bundles.

Usable Framework style Python installations
-------------------------------------------

* System-wide Python bundled with Mac OSX
* ``brew install python --framework``

The following will **not** work:

* ``brew install python`` (does not create a Framework style build)

References
----------

* https://github.com/pypa/virtualenv/issues/54
* http://stackoverflow.com/questions/3692928/why-doesnt-the-save-button-work-on-a-matplotlib-plot
* http://code.google.com/p/iterm2/issues/detail?id=1680
