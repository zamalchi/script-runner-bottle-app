#!/usr/bin/env python

# from __future__ import print_function
import code
import readline

# context provides the slurm module
# from context import slurm
import modu.slurm as slurm
import modu.color_printer as cp

print("----------------------------------------------------------------------")
cp.printWarn("from context import slurm")
cp.printWarn("states = slurm.Slurm.getNonEmptyStates()")
print("----------------------------------------------------------------------")

states = slurm.Slurm.getNonEmptyStates()

vars = globals().copy()
vars.update(locals())
shell = code.InteractiveConsole(vars)
shell.interact()
