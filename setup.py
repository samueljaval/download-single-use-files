"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app

This file is to use if you want to make a standalone app with py2app
You should use this setup.py file instead of the one generated by py2applet --make-setup main.py
because I have included 'packages': ['rumps','pync'] which is very important
"""
from setuptools import setup

APP = ['single_use_files.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'LSUIElement': True,
    },
    'packages': ['rumps','pync'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
