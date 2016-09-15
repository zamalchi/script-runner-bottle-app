#!/usr/bin/python

import argparse

from src.bottle import run

from src.main import *

# argparse
parser = argparse.ArgumentParser()
parser.add_argument('-p', help = "Port number", action="store", dest="p", required = True)
parser.add_argument('-a', help = "Host address", action="store", dest="a", required = True)

args = parser.parse_args()

port = args.p
address = args.a

run(host=address, port=port, debug=True)
