#!/usr/bin/env python

from setuptools import setup

setup(
    name='fix-osx-virtualenv',
    version="0.1",
    description='Fixes virtualenvs on Mac OSX to be GUI friendly',
    long_description="",
    license='MIT',
    author='Matthew Scott and Contributors',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    packages=['install_pythonw'],
    entry_points={
        'console_scripts': ['fix-osx-virtualenv = install_pythonw:run_main'],
    },
    package_data={'install_pythonw': [
        'pythonw.c',
    ]},
)
