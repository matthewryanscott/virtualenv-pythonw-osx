virtualenv-pythonw-osx
===========================

Some GUIs Pythona apps don't work right, unless ``pythonw`` is in an app bundle.

This script only fixes virtualenvs based on Framework style installs (bundles)

Framework Installs:
---------------------

* the default OSX install
* ``brew install python --framework``

But **not**:

* ``brew install python``, which we can't fix using this method



CF:

https://github.com/pypa/virtualenv/issues/54
http://stackoverflow.com/questions/3692928/why-doesnt-the-save-button-work-on-a-matplotlib-plot
http://code.google.com/p/iterm2/issues/detail?id=1680

This code attempts to fix this issue, by making sure both ``python`` and ``pythonw`` get
compiled like app bundles.
