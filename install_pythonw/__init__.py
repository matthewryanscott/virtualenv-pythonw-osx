#!/usr/bin/env python

"""

Some GUIs don't work right, unless the python is in an app bundle.

This script only fixes virtualenvs based on Framework style installs (bundles)

CF:

https://github.com/pypa/virtualenv/issues/54
http://stackoverflow.com/questions/3692928/why-doesnt-the-save-button-work-on-a-matplotlib-plot
http://code.google.com/p/iterm2/issues/detail?id=1680

This code attempts to fix this issue, by making sure both ``python`` and ``pythonw`` get
compiled like app bundles.
"""


import os
from os import path
import shutil
from subprocess import call
import sys
import struct

PYTHON_ARCH = 8 * struct.calcsize("P")
ARCHS = {32:'i386',64:'x86_64'}

USAGE = """
Usage: install_pythonw.py ROOT_OF_PARTICULAR_VIRTUALENV
(if you are in the virtualenv right now, try:

    $ which python

for me: /Users/me/venvs/py27/bin/python

    $ python install_pythonw.py /Users/me/venvs/py27/

or

    $ python install_pythonw.py `which python`/../..


"""

BREW_NOTE = """

if this virtualenv is based on the Python installation from Homebrew,
you might want to install "Framework style".  This script only fixes
virtualenvs based on OSX Framework-style installs.

    $ brew install python --framework


"""

def main(argv):
    if len(argv) != 2:
        print(USAGE)
        sys.exit(1)
    env_path = path.abspath(argv[1])
    script_path = path.abspath(path.dirname(__file__))

    # If Python.app already exists, exit.
    python_app_dest = path.join(env_path, 'Python.app')
    if path.exists(python_app_dest):
        print(python_app_dest, 'already exists; exiting.')
        return 1
    # Find pythonw.c in script path.
    pythonw_c = path.join(script_path, 'pythonw.c')
    if not path.exists(pythonw_c):
        print(pythonw_c, 'does not exist; exiting.')
        return 1
    # Find .Python symlink.
    dot_python = path.join(env_path, '.Python')
    if not path.exists(dot_python):
        print(dot_python, 'does not exist; exiting.')
        return 1
    # Find symlink source.
    dot_python_src = os.readlink(dot_python)
    if not path.exists(dot_python_src):
        print(dot_python_src, 'does not exist; exiting.')
        print(BREW_NOTE)
        return 1
    # Find Python.app in PARDIR/Resources/
    python_app_src = path.join(
        path.dirname(dot_python_src), 'Resources', 'Python.app')
    if not path.exists(python_app_src):
        print(python_app_src, 'does not exist; exiting.')
        return 1
    # Copy Python.app to env_path
    shutil.copytree(python_app_src, python_app_dest)
    # Change install names in Python.app binary.
    pythonw_executable = path.join(
        python_app_dest, 'Contents', 'MacOS', 'Python')
    call([
        'install_name_tool',
        '-change',
        dot_python_src,
        dot_python,
        pythonw_executable,
        ])
    # Compile pythonw to bin directory.
    for name in ['python','pythonw']:
        pythonw_dest = path.join(env_path, 'bin', name)
        call([
            'cc',
            '-arch', ARCHS[PYTHON_ARCH],
            '-DPYTHONWEXECUTABLE="' + pythonw_executable + '"',
            '-o',
            pythonw_dest,
            pythonw_c,
            ])

    print("finished!  App bundle created at:  " + python_app_dest)


def run_main():
    sys.exit(main(sys.argv))


if __name__ == '__main__':
    run_main()
