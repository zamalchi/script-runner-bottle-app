
HOST=172.16.1.254
PORT=19191

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

# COMPILING
# ----------------------------------------------------------------------
scss:
	./src/scss-to-css-transpiler.sh

scss-watch:
	./src/scss-to-css-transpiler.sh --watch

# MISC
# ----------------------------------------------------------------------
clean:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . -name '*~' -exec rm --force  {} +

# HELP
# ----------------------------------------------------------------------
help:
	@echo "----------------------------------------------------------------------"
	@echo "HOST ADDRESS : http://$(HOST):$(PORT)"
	@echo "----------------------------------------------------------------------"
	@echo "    run"
	@echo "        Run the slurm server."
	@echo "    debug"
	@echo "        Run the slurm server in debug mode."
	@echo "    debug-watch"
	@echo "        Run the slurm server in debug mode with live reload."
	@echo "    local"
	@echo "        Run the slurm server on localhost in debug mode."
	@echo "----------------------------------------------------------------------"
	@echo "    test"
	@echo "        Run testing suite."
	@echo "    test-slurm"
	@echo "        Run modu.tests.slurm-test. Tests integrity of slurm data parsing."
	@echo "    test-slurm-shell"
	@echo "        Run modu.tests.slurm-test-shell. Returns an interactive shell."
	@echo "----------------------------------------------------------------------"
	@echo "    clean"
	@echo "        Remove python artifacts."
	@echo "----------------------------------------------------------------------"

# ----------------------------------------------------------------------

.PHONY: clean test-slurm test-slurm-shell