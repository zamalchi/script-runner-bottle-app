#!/bin/bash

parent_path=$( cd "$(dirname "${BASH_SOURCE}")" ; pwd -P )

cd $parent_path

sass --watch ./base.scss:../../static/css/main.css