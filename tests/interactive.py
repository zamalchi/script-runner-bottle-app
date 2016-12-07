#!/usr/bin/env python

import code
import readline

import modu.slurm as slurm

print "import modu.slurm as slurm"
print "states = slurm.Slurm.getNonEmptyStates()"
print "----------------------------------------------------------------------"

states = slurm.Slurm.getNonEmptyStates()

vars = globals().copy()
vars.update(locals())
shell = code.InteractiveConsole(vars)
shell.interact()
