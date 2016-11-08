#!/usr/bin/python

import unittest

from classes.Slurm import Slurm

reservations = [
"""
ReservationName=root_6 StartTime=2016-12-06T08:00:00 EndTime=2016-12-06T18:00:00 Duration=10:00:00
   Nodes=node[001-471] NodeCnt=471 CoreCnt=4434 Features=(null) PartitionName=(null) Flags=MAINT,IGNORE_JOBS,SPEC_NODES
   Users=root Accounts=(null) Licenses=(null) State=INACTIVE""",
"""
ReservationName=gene_neu_reservation1 StartTime=2016-11-01T10:05:18 EndTime=2016-11-13T00:00:00 Duration=11-14:54:42
   Nodes=node001,node002 NodeCnt=2 CoreCnt=16 Features=(null) PartitionName=(null) Flags=SPEC_NODES
   Users=ac,root,apoorve,cooperman,jiajun,rohgarg Accounts=(null) Licenses=(null) State=ACTIVE"""
]
testReservation = {}
testReservation["name"] = ["root_6", "gene_neu_reservation1"]
testReservation["nodeCount"] = [471, 2]


class TestSlurmSuite(unittest.TestCase):

    # def test_state(self):
    #     self.assertEqual('foo'.upper(), 'FOO')
    #
    # def test_entry(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    def test_reservation(self):
        i = 0
        for each in reservations:
            obj = Slurm.Reservation(each)

            self.assertTrue(obj.__class__.__name__ == "Reservation")
            self.assertTrue(obj.name == testReservation["name"][i])
            self.assertTrue(len(obj.nodes) == testReservation["nodeCount"][i])
            self.assertTrue(type(obj.data) is dict)

            i += 1

        print("OK : Reservation Tests")

        # with self.assertRaises(TypeError):
        #     s.split(2)


if __name__ == '__main__':
    print
    unittest.main()
