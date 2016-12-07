#!/bin/bash

SRC_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

scss_file="${SRC_DIR}/scss/base.scss"
css_file="${SRC_DIR}/../static/css/main.css"

sass ${1} ${scss_file}:${css_file}