#!/usr/bin/env python

import unittest

import modu.slurm as slurm
import slurmTest

class MockTestSlurmSuite(slurmTest.TestSlurmSuite):
  dataSource = slurm.Mock

if __name__ == '__main__':
  print("----------------------------------------------------------------------")
  unittest.main()