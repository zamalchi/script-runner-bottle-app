#!/usr/bin/env python

# from __future__ import print_function
import code
import readline

# context provides the slurm module
# from context import slurm
import modu.slurm as slurm
import modu.color_printer as cp

print("----------------------------------------------------------------------")
cp.printWarn("import modu.slurm as slurm")
cp.printWarn("import modu.color_printer as cp")
cp.printWarn("states = slurm.Mock.getNonEmptyStates()")
cp.printWarn("reservations = slurm.Mock.getReservations()")
print("----------------------------------------------------------------------")

states = slurm.Mock.getNonEmptyStates()
reservations = slurm.Mock.getReservations()

vars = globals().copy()
vars.update(locals())
shell = code.InteractiveConsole(vars)
shell.interact()
