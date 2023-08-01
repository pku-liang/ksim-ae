.phony: build clean-build run clean-run

build:
	$(MAKE) -C runs build
clean-build:
	$(MAKE) -C runs clean

run:
	python benchmark.py
clean-run:
	rm -rf results

.phony: prepare-setup setup distclean

prepare-setup: prepare-setup-sims prepare-setup-tools
prepare-setup-%:
	$(MAKE) -C $* prepare

setup: setup-sims setup-tools
setup-%:
	$(MAKE) -C $* setup

distclean:
	$(MAKE) -C sims clean
	$(MAKE) -C tools clean
	$(MAKE) -C runs clean