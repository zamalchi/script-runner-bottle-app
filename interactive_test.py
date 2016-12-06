#!/usr/bin/env python

import readline
import code

from modu.slurm import *

all = Slurm.getNonEmptyStates()


vars = globals().copy()
vars.update(locals())
shell = code.InteractiveConsole(vars)
shell.interact()
