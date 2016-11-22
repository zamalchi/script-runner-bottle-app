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

        for s in states:
            self.assertTrue(s.__class__.__name__ == "State")
        print("OK : States are all Slurm.State objects")

        for s in states:
            self.assertTrue(s.entries)
        print("OK : All states have entries")

        for s in states:
            for e in s.entries:
                self.assertTrue(e.__class__.__name__ == "Entry")
        print("OK : All entries are Slurm.Entry objects")



    def test_reservation(self):
        print
        i = 0
        if self.liveData:
            rawOutput["reservations"] = Slurm.getScontrolShowReservation()
            print(formatStr("Reservations:") + "(LIVE)")

        else:
            print(formatStr("Reservations:") + "(MOCK)")

        for each in rawOutput["reservations"]:
            obj = Slurm.Reservation(each)

            self.assertTrue(obj.__class__.__name__ == "Reservation")

            if not self.liveData:
                self.assertTrue(obj.name == tests["reservations"]["name"][i])
                self.assertTrue(len(obj.nodes) == tests["reservations"]["nodeCount"][i])
                self.assertTrue(obj.state == tests["reservations"]["state"][i])
                self.assertTrue(type(obj.data) is dict)

            i += 1

        print(formatStr("Reservations:") + "OK")

if __name__ == '__main__':

    # if len(sys.argv) > 1:
    #     if sys.argv.pop() == "live":
    #         TestSlurmSuite.liveData = True

    print("----------------------------------------------------------------------")
    unittest.main()
