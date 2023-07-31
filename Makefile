.phony: build-cases clean-cases

build-cases:
	$(MAKE) -C runs build
clean-cases:
	$(MAKE) -C runs clean

run-all:
	python benchmark.py
clean-run:
	rm -rf results

.phony: setup setup-sims setup-tools clean-setup-build

setup: setup-sims setup-tools

setup-sims:
	$(MAKE) -C sims setup

setup-tools:
	$(MAKE) -C tools setup

clean-tool-build:
	$(MAKE) -C sims cleanbuild
clean:
	$(MAKE) -C sims clean
	$(MAKE) -C tools clean
	$(MAKE) -C runs clean