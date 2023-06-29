
build:
	$(MAKE) -C runs build
clean:
	$(MAKE) -C runs clean

setup: setup-sims setup-tools

setup-sims:
	$(MAKE) -C sims setup

setup-tools:
	$(MAKE) -C tools setup
