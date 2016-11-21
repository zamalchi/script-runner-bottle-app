#!/bin/bash

parent_path=$( cd "$(dirname "${BASH_SOURCE}")" ; pwd -P )

cd $parent_path

/usr/bin/env python run.py -a 172.16.1.254 -p 19191
