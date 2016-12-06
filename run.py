#!/usr/bin/python

import argparse

from src.main import *

from src.bottle import run

# argparse
parser = argparse.ArgumentParser()
parser.add_argument('-p', help = "Port number", action="store", dest="p", required = True)
parser.add_argument('-a', help = "Host address", action="store", dest="a", required = True)
parser.add_argument('-d', help = "Dev mode", action="store_true", required = False)


args = parser.parse_args()

port = args.p
address = args.a
devMode = args.d

if devMode:
    setDevMode(devMode)

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
print("ROOT DIR IN RUN.PY : {}".format(ROOT_DIR))

setRootDir(ROOT_DIR)

run(host=address, port=port, debug=True)
