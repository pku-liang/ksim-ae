export INSTALL_PREFIX ?= $(shell realpath ../install)

setup: $(INSTALL_PREFIX)/bin/firtool $(INSTALL_PREFIX)/bin/ksim

prepare:
	git submodule deinit -f ksim; git submodule update --init ksim
	git -C ksim submodule update --init
	git -C ksim/third_party/circt submodule update --init
	cd ksim/third_party && ./setup-lemon.sh
	touch $@

$(INSTALL_PREFIX)/bin/ksim: prepare $(INSTALL_PREFIX)/bin/firtool
	cd ksim && ([ -d build ] || mkdir build)
	cd ksim/build && cmake .. -DCMAKE_INSTALL_PREFIX=$(INSTALL_PREFIX)
	$(MAKE) -C ksim/build

$(INSTALL_PREFIX)/bin/firtool: prepare
	cd ksim/third_party && ./setup-circt.sh

clean-build:
	git submodule deinit -f ksim
	rm -rf prepare

clean: clean-build