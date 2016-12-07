#!/usr/bin/env python

"""
This is imported by the test files
to provide context for the directory structure

usage:
from .context import module
"""

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import modu.slurm as slurm