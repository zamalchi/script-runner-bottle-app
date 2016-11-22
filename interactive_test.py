#!/usr/bin/env python

import readline
import code

from classes.Slurm import *

all = Slurm.getNonEmptyStates()


vars = globals().copy()
vars.update(locals())
shell = code.InteractiveConsole(vars)
shell.interact()
