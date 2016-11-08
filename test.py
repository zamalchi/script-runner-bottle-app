#!/usr/bin/python

import unittest
import sys

from classes.Slurm import Slurm

# import argparse
#
# # argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('-l', help = "Live data mode", action="store_true", required = False)
#
# args = parser.parse_args()
# liveData = args.l

######################################################################
######################################################################
# SINFO / SCONTROL DATA HARDCODED FOR TESTING
# KEYS ARE : "states", "reservations"
rawOutput = {}
# fields pulled from the data to test against instantiated objects (to ensure correct parsing)
tests = {}

# *************************

rawOutput["states"] = {
    "allocated" : """
node[001,003-016,027,030-036,055-073,083-086,088,091-100,102-105,112-120,128-141,143-144,146-160,162-169,171-194,196-229,236-238,254-259,261-271,280-281,290-292,296,298-299,309,313-316,331-338,343-352,356-362,364-386,388-390,393-395,403-422,429-431,434-464]\tUnknown             \tnone
""",
    "maint" : """
node[019-026,074-080,106-108]\t2016-10-13T11:06:00 \tNot responding
node[087,122-123]\t2016-10-13T17:36:01 \tNot responding
node[101,235,279,317-320]\tUnknown             \tnone
node[161,170,195]\t2016-09-01T10:30:39 \tmoc NSDI/BMI paper until Sept 24,2016, persistent 3 - CNH 20160901
""",
    "down" : """
node[017-018,037-054,089-090]\t2016-07-18T08:16:27 \tLLGRID
node[019-026,074-080,106-108]\t2016-10-13T11:06:00 \tNot responding
node[087,122-123]\t2016-10-13T17:36:01 \tNot responding
node[109-111]\t2016-05-18T15:13:50 \tLLGRID
node[121,124]\t2016-11-03T16:29:44 \tNot responding
node125\t2016-11-04T14:50:33 \tNot responding
node126\t2016-11-04T11:50:33 \tNot responding
node[161,170,195]\t2016-09-01T10:30:39 \tmoc NSDI/BMI paper until Sept 24,2016, persistent 3 - CNH 20160901
node426\t2016-11-07T13:43:04 \tbring it to campus
node427\t2016-11-07T13:43:13 \tbring it to campus
node433\t2016-11-01T10:15:28 \tmove
"""
}

# *************************


rawOutput["reservations"] = [
"ReservationName=cnh_omnipath_testing StartTime=2016-07-11T09:45:59 EndTime=2017-07-11T09:45:59 Duration=365-00:00:00 Nodes=node[317-320] NodeCnt=4 CoreCnt=40 Features=(null) PartitionName=(null) Flags=MAINT,SPEC_NODES Users=root,cnh Accounts=(null) Licenses=(null) State=ACTIVE",
"ReservationName=root_1 StartTime=2016-08-11T16:40:06 EndTime=2017-08-11T16:40:06 Duration=365-00:00:00 Nodes=node235,node101,node279 NodeCnt=3 CoreCnt=26 Features=(null) PartitionName=(null) Flags=MAINT,IGNORE_JOBS,SPEC_NODES Users=root,sb,ac,gshomo,ghassemi,wha,fridman,denru,cnh,josephe,bernauer,emgolos Accounts=(null) Licenses=(null) State=ACTIVE",
"ReservationName=flexalloc_moc_20161012 StartTime=2016-10-13T10:25:48 EndTime=2016-11-30T10:25:48 Duration=48-01:00:00 Nodes=node019,node020,node021,node022,node023,node024,node025,node026,node074,node075,node076,node077,node078,node079,node080,node106,node107,node108,node087,node122,node123,node170,node161,node195 NodeCnt=24 CoreCnt=192 Features=(null) PartitionName=(null) Flags=MAINT,IGNORE_JOBS,SPEC_NODES Users=root Accounts=(null) Licenses=(null) State=ACTIVE",
"ReservationName=root_6 StartTime=2016-12-06T08:00:00 EndTime=2016-12-06T18:00:00 Duration=10:00:00 Nodes=node[001-471] NodeCnt=471 CoreCnt=4434 Features=(null) PartitionName=(null) Flags=MAINT,IGNORE_JOBS,SPEC_NODES Users=root Accounts=(null) Licenses=(null) State=INACTIVE",
"ReservationName=gene_neu_reservation1 StartTime=2016-11-01T10:05:18 EndTime=2016-11-13T00:00:00 Duration=11-14:54:42 Nodes=node001,node002 NodeCnt=2 CoreCnt=16 Features=(null) PartitionName=(null) Flags=SPEC_NODES Users=ac,root,apoorve,cooperman,jiajun,rohgarg Accounts=(null) Licenses=(null) State=ACTIVE"
]

tests["reservations"] = {}
tests["reservations"]["name"] = ["cnh_omnipath_testing", "root_1", "flexalloc_moc_20161012", "root_6", "gene_neu_reservation1"]
tests["reservations"]["nodeCount"] = [4, 3, 24, 471, 2]
tests["reservations"]["state"] = ["ACTIVE", "ACTIVE", "ACTIVE", "INACTIVE", "ACTIVE"]

######################################################################
######################################################################

def formatStr(raw):
    return raw.ljust(25)

######################################################################
######################################################################

class TestSlurmSuite(unittest.TestCase):

    liveData = False

    def test_state(self):
        print
        if self.liveData:
            rawOutput["states"] = Slurm.getNonEmptyStates()
            print(formatStr("States and Entries:") + "(LIVE)")
        else:
            print(formatStr("States and Entries:") + "(MOCK)")

        for key in rawOutput["states"]:
            obj = Slurm.State(key, rawOutput["states"][key])

            self.assertTrue(obj.__class__.__name__ == "State")
            self.assertTrue(obj.name in Slurm.states)
            self.assertTrue(obj.hasEntries())
            self.assertTrue(type(obj.entries) is list)

            for entry in obj.entries:
                self.assertTrue(entry.__class__.__name__ == "Entry")
                self.assertTrue(entry.nodes)
                self.assertTrue(entry.time)
                self.assertTrue(entry.reason)

        print(formatStr("States and Entries:") + "OK")


    def test_reservation(self):
        print
        i = 0
        if self.liveData:
            rawOutput["reservations"] = Slurm.getReservations()
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

    if len(sys.argv) > 1:
        if sys.argv.pop() == "live":
            TestSlurmSuite.liveData = True

    print("************************")
    unittest.main()
