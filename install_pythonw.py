#!/usr/bin/env python

import os
from os import path
import shutil
from subprocess import call
import sys


USAGE = """
Usage: install_pythonw.py ENVPATH
"""


def main(env_path, script_path):
    # If Python.app already exists, exit.
    python_app_dest = path.join(env_path, 'Python.app')
    if path.exists(python_app_dest):
        print python_app_dest, 'already exists; exiting.'
        return 1
    # Find pythonw.c in script path.
    pythonw_c = path.join(script_path, 'pythonw.c')
    if not path.exists(pythonw_c):
        print pythonw_c, 'does not exist; exiting.'
        return 1
    # Find .Python symlink.
    dot_python = path.join(env_path, '.Python')
    if not path.exists(dot_python):
        print dot_python, 'does not exist; exiting.'
        return 1
    # Find symlink source.
    dot_python_src = os.readlink(dot_python)
    if not path.exists(dot_python_src):
        print dot_python_src, 'does not exist; exiting.'
        return 1
    # Find Python.app in PARDIR/Resources/
    python_app_src = path.join(
        path.dirname(dot_python_src), 'Resources', 'Python.app')
    if not path.exists(python_app_src):
        print python_app_src, 'does not exist; exiting.'
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
    pythonw_dest = path.join(env_path, 'bin', 'pythonw')
    call([
        'cc',
        '-arch', 'i386', '-arch', 'x86_64',
        '-DPYTHONWEXECUTABLE="' + pythonw_executable + '"',
        '-o',
        pythonw_dest,
        pythonw_c,
        ])


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print USAGE
        sys.exit(1)
    env_path = path.abspath(sys.argv[1])
    script_path = path.abspath(path.dirname(sys.argv[0]))
    sys.exit(main(env_path, script_path))
