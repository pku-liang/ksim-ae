export INSTALL_PREFIX ?= ../install

setup: $(INSTALL_PREFIX)/bin/firtool $(INSTALL_PREFIX)/bin/ksim

prepare:
	git submodule deinit -f ksim; git submodule update --init ksim
	git -C ksim submodule update --init
	git -C ksim/third_party/circt submodule update --init
	cd ksim/third_party && ./setup-lemon.sh
	touch $@

$(INSTALL_PREFIX)/bin/ksim: prepare $(INSTALL_PREFIX)/bin/firtool

$(INSTALL_PREFIX)/bin/firtool: prepare
	cd ksim/third_party && ./setup-circt.sh

clean-build:
	git submodule deinit -f ksim
	rm -rf prepare

clean: clean-build