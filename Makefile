
HOST=172.16.1.254
PORT=19191

LBLUE=`echo -e "\033[1;34m"`
LGREEN=`echo -e "\033[1;32m"`
PURPLE=`echo -e "\033[35m"`
WHITE=`echo -e "\033[1;37m"`
NORMAL=`echo -e "\033[m"`

# SERVING
# ----------------------------------------------------------------------
run:
	/usr/bin/env python app.py -a $(HOST) -p $(PORT)

debug:
	/usr/bin/env python app.py -a $(HOST) -p $(PORT) -d

debug-watch:
	/usr/bin/env python app.py -a $(HOST) -p $(PORT) -d -r

local:
	/usr/bin/env python app.py -a localhost -p 8081 -d

# TESTING
# ----------------------------------------------------------------------
test: test-slurm test-slurm-shell

test-slurm: clean
	/usr/bin/env python -m modu.tests.slurm-test

test-slurm-shell: clean
	/usr/bin/env python -m modu.tests.slurm-test-shell

# COMPILING / TRANSPILING
# ----------------------------------------------------------------------
scss:
	./src/scss/transpiler.sh

scss-watch:
	./src/scss/transpiler.sh --watch

# MISC
# ----------------------------------------------------------------------
clean:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . -name '*~' -exec rm --force  {} +

# HELP
# ----------------------------------------------------------------------
help:
	@echo "${PURPLE}----------------------------------------------------------------------${NORMAL}"
	@echo "    HOST ADDRESS : ${WHITE}http://$(HOST):$(PORT)${NORMAL}"
	@echo "${PURPLE}----------------------------------------------------------------------${NORMAL}"
	@echo "    ${LGREEN}run${NORMAL}"
	@echo "        ${LBLUE}Run the slurm server.${NORMAL}"
	@echo "    ${LGREEN}debug${NORMAL}"
	@echo "        ${LBLUE}Run the slurm server in debug mode.${NORMAL}"
	@echo "    ${LGREEN}debug-watch${NORMAL}"
	@echo "        ${LBLUE}Run the slurm server in debug mode with live reload.${NORMAL}"
	@echo "    ${LGREEN}local${NORMAL}"
	@echo "        ${LBLUE}Run the slurm server on localhost in debug mode.${NORMAL}"
	@echo "${PURPLE}----------------------------------------------------------------------${NORMAL}"
	@echo "    ${LGREEN}test${NORMAL}"
	@echo "        ${LBLUE}Run testing suite.${NORMAL}"
	@echo "    ${LGREEN}test-slurm${NORMAL}"
	@echo "        ${LBLUE}Run modu.tests.slurm-test. Tests integrity of slurm data parsing.${NORMAL}"
	@echo "    ${LGREEN}test-slurm-shell${NORMAL}"
	@echo "        ${LBLUE}Run modu.tests.slurm-test-shell. Returns an interactive shell.${NORMAL}"
	@echo "${PURPLE}----------------------------------------------------------------------${NORMAL}"
	@echo "    ${LGREEN}scss${NORMAL}"
	@echo "        ${LBLUE}Compile scss source files to css static files.${NORMAL}"
	@echo "    ${LGREEN}scss-watch${NORMAL}"
	@echo "        ${LBLUE}Watch for changes and recompile scss.${NORMAL}"
	@echo "${PURPLE}----------------------------------------------------------------------${NORMAL}"
	@echo "    ${LGREEN}clean${NORMAL}"
	@echo "        ${LBLUE}Remove python artifacts.${NORMAL}"
	@echo "${PURPLE}----------------------------------------------------------------------${NORMAL}"

# ----------------------------------------------------------------------

.PHONY: clean test-slurm test-slurm-shell