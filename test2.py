#!/usr/bin/env python

import unittest
import sys

from classes.Slurm import Slurm

######################################################################
######################################################################

def formatStr(raw):
    return raw.ljust(25)

######################################################################
######################################################################

class TestSlurmSuite(unittest.TestCase):

    def test_state(self):
        states = Slurm.getNonEmptyStates()

        self.assertTrue(states)
        print("OK : List of states exists")

        for s in states.values():
            self.assertTrue(s.__class__.__name__ == "State")
        print("OK : States are all Slurm.State objects")

        for s in states.values():
            self.assertTrue(s.hasEntries())
        print("OK : All states have entries")

        for s in states.values():
            for e in s.entries:
                self.assertTrue(e.__class__.__name__ == "Entry")
        print("OK : All entries are Slurm.Entry objects")

        for s in states.values():
            for e in s.entries:
                self.assertTrue(e.nodes and e.time and e.reason)
        print("OK : All entries have nodes, time, and reason attributes")

    def test_reservation(self):
        reservations = Slurm.getReservations()

        self.assertTrue(reservations)
        print("OK : List of reservations exists")

        for r in reservations:
            self.assertTrue(r.name and r.nodes and r.state and r.data)
        print("OK : All reservations have name, nodes, state, and data attributes")

        for r in reservations:
            for n in r.nodes:
                self.assertTrue(n == Slurm.normalizeNodeName(n))
        print("OK : All reserved nodes are in normalized format")

        for r in reservations:
            self.assertTrue(type(r.data) is dict)
        print("OK : All reservations' data attribute are type dictionary")

    def test_node(self):
        nodes = []
        nodes.append(Slurm.Node("034"))
        nodes.append(Slurm.Node(100))
        nodes.append(Slurm.Node("node123"))

        for n in nodes:
            self.assertTrue(n.__class__.__name__ == "Node")
        print("OK : All nodes are Slurm.Node objects")

        for n in nodes:
            self.assertTrue(n.found or not n.data)
        print("OK : All nodes either found or (if not found) have no data")

        for n in nodes:
            if n.found:
                self.assertTrue(n.state and n.data)
        print("OK : All found nodes have state and data attributes")

        for n in nodes:
            self.assertTrue(type(n.data) is dict)
        print("OK : All nodes' data attribute are type dictionary")

        for n in nodes:
            self.assertTrue(n.name == Slurm.normalizeNodeName(n.name))
        print("OK : All nodes' names are in normalized format")



if __name__ == '__main__':

    # if len(sys.argv) > 1:
    #     if sys.argv.pop() == "live":
    #         TestSlurmSuite.liveData = True

    print("----------------------------------------------------------------------")
    unittest.main()
