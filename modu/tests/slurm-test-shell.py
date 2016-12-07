#!/usr/bin/env python

from __future__ import print_function
import code
import readline

# context provides the slurm module
from context import slurm

print("----------------------------------------------------------------------")
print("from context import slurm")
print("states = slurm.Slurm.getNonEmptyStates()")
print("----------------------------------------------------------------------")

states = slurm.Slurm.getNonEmptyStates()

vars = globals().copy()
vars.update(locals())
shell = code.InteractiveConsole(vars)
shell.interact()
