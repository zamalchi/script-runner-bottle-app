
HOST=172.16.1.254
PORT=19191

.PHONY: clean-pyc test-slurm test-slurm-shell

run:
	/usr/bin/env python main.py -a $(HOST) -p $(PORT)

debug:
	/usr/bin/env python main.py -a $(HOST) -p $(PORT) -d

debug-watch:
	/usr/bin/env python main.py -a $(HOST) -p $(PORT) -d -r

local:
	/usr/bin/env python main.py -a localhost -p 8081 -d

test: test-slurm test-slurm-shell

test-slurm: clean-pyc
	/usr/bin/env python -m modu.tests.slurm-test

test-slurm-shell: clean-pyc
	/usr/bin/env python -m modu.tests.slurm-test-shell

clean:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . -name '*~' -exec rm --force  {} +

help:
	@echo "----------------------------------------------------------------------"
	@echo "    run"
	@echo "        Run the slurm server on $(HOST):$(PORT)."
	@echo "    debug"
	@echo "        Run the slurm server on $(HOST):$(PORT) in debug mode."
	@echo "    debug-watch"
	@echo "        Run the slurm server on $(HOST):$(PORT) in debug mode with live reload."
	@echo "    local"
	@echo "        Run the slurm server on localhost in debug mode."
	@echo "    test"
	@echo "        Run testing suite."
	@echo "    test-slurm"
	@echo "        Run modu.tests.slurm-test. Tests integrity of slurm data parsing."
	@echo "    test-slurm-shell"
	@echo "        Run modu.tests.slurm-test-shell. Returns an interactive shell."
	@echo "    clean"
	@echo "        Remove python artifacts."
	@echo "----------------------------------------------------------------------"
