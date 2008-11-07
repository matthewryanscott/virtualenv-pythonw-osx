#!/usr/bin/env python

import os
import sys


USAGE = """
Usage: install_pythonw ENVPATH
"""


def main(env_path, script_path):
    # If Python.app already exists, exit.
    # Find .Python symlink.
    # Find symlink destination.
    # Find Python.app in PARDIR/Resources/
    # Copy Python.app to env_path
    # Change install names in Python.app binary.
    # Find pythonw.c in script path.
    # Compile pythonw to bin directory.
    pass


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print USAGE
        sys.exit(1)
    env_path = os.path.abspath(sys.argv[1])
    script_path = os.path.abspath(os.path.dirname(sys.argv[0]))
    sys.exit(main(env_path, script_path))
