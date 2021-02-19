#!/usr/bin/python

from setuptools import setup

setup(name='checknml',
      version='1.0',
      # list folders, not files
      packages=['checknml',
                'tests'],
      scripts=['bin/checknml_app.py'],
      )
