#!/usr/bin/env python

import argparse
import sys
import unittest

import modu.slurm as slurm
import modu.color_printer as cp

######################################################################
######################################################################

def formatStr(raw):
  return raw.ljust(25)

######################################################################
######################################################################

class TestSlurmSuite(unittest.TestCase):

  dataSource = slurm.Slurm

  def test_state(self):
    print("\n --- STATE TESTS ({}) ---".format(self.dataSource))
    states = self.dataSource.getNonEmptyStates()

    self.assertTrue(states)
    cp.printOK("OK : List of states exists")

    for s in states.values():
      self.assertTrue(s.__class__.__name__ == "State")
    cp.printOK("OK : All states are State objects")

    for s in states.values():
      self.assertTrue(s.hasEntries())
    cp.printOK("OK : All states have entries")

    for s in states.values():
      for e in s.entries:
        self.assertTrue(e.__class__.__name__ == "Entry")
    cp.printOK("OK : All entries are Entry objects")

    for s in states.values():
      for e in s.entries:
        self.assertTrue(e.nodes and e.time and e.reason)
    cp.printOK("OK : All entries have nodes, time, and reason attributes")

  ############################################################################################

  def test_reservation(self):
    print("\n --- RESERVATION TESTS ({}) ---".format(self.dataSource))
    reservations = self.dataSource.getReservations()

    self.assertTrue(reservations)
    cp.printOK("OK : List of reservations exists")

    for r in reservations:
      self.assertTrue(r.__class__.__name__ == "Reservation")
    cp.printOK("OK : All reservations are Reservation objects")

    for r in reservations:
      self.assertTrue(r.name and r.nodes and r.state and r.data)
    cp.printOK("OK : All reservations have name, nodes, state, and data attributes")

    for r in reservations:
      for n in r.nodes:
        self.assertTrue(n == slurm.Slurm.normalizeNodeName(n))
    cp.printOK("OK : All reserved nodes are in normalized format")

    for r in reservations:
      self.assertTrue(type(r.data) is dict)
    cp.printOK("OK : All reservations' data attribute are type dictionary")

  ############################################################################################

  def test_node(self):
    print("\n --- NODE TESTS ({}) ---".format(self.dataSource))
    nodes = []
    if self.dataSource == "modu.slurm.Mock":
      nodes.append(self.dataSource.getNode())
    else:
      nodes.append(TestSlurmSuite.dataSource.getNode("034"))
      nodes.append(TestSlurmSuite.dataSource.getNode(100))
      nodes.append(TestSlurmSuite.dataSource.getNode("node123"))

    for n in nodes:
      self.assertTrue(n.__class__.__name__ == "Node")
    cp.printOK("OK : All nodes are Node objects")

    for n in nodes:
      self.assertTrue(n.found or not n.data)
    cp.printOK("OK : All nodes either found or (if not found) have no data")

    for n in nodes:
      if n.found:
        self.assertTrue(n.state and n.data)
    cp.printOK("OK : All found nodes have state and data attributes")

    for n in nodes:
      self.assertTrue(type(n.data) is dict)
    cp.printOK("OK : All nodes' data attribute are type dictionary")

    for n in nodes:
      self.assertTrue(n.name == slurm.Slurm.normalizeNodeName(n.name))
    cp.printOK("OK : All nodes' names are in normalized format")

  ############################################################################################

if __name__ == '__main__':
  print("----------------------------------------------------------------------")
  unittest.main()
