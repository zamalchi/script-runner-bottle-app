#!/usr/bin/python

import argparse

from src.main import *

from src.bottle import run

# argparse
parser = argparse.ArgumentParser()
parser.add_argument('-p', help = "Port number", action="store", dest="p", required = True)
parser.add_argument('-a', help = "Host address", action="store", dest="a", required = True)

args = parser.parse_args()

port = args.p
address = args.a

run(host=address, port=port, debug=True)
