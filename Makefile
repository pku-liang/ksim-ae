.phony: build-cases clean-cases

build-cases:
	$(MAKE) -C runs build
clean-cases:
	$(MAKE) -C runs clean

.phony: setup setup-sims setup-tools clean-setup-build

setup: setup-sims setup-tools

setup-sims:
	$(MAKE) -C sims setup

setup-tools:
	$(MAKE) -C tools setup

clean-setup-build:
	$(MAKE) -C sims cleanbuild