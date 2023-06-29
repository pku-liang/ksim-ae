
build:
	$(MAKE) -C runs build

setup: setup-sims setup-tools

setup-sims:
	$(MAKE) -C sims setup

setup-tools:
	$(MAKE) -C tools setup
