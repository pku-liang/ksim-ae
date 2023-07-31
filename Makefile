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

prepare-setup:
setup: setup-sims setup-tools

prepare-setup-%:
	$(MAKE) -C $* prepare
setup-%:
	$(MAKE) -C $* setup

clean-tool-build:
	$(MAKE) -C sims cleanbuild
clean:
	$(MAKE) -C sims clean
	$(MAKE) -C tools clean
	$(MAKE) -C runs clean