INSTALL_PREFIX ?= ../install

setup: $(INSTALL_PREFIX)/bin/verilator

prepare:
	git submodule deinit -f verilator; git submodule update --init verilator
	touch $@

$(INSTALL_PREFIX)/bin/verilator: prepare $(wildcard verilator/src/**/*)
	cd verilator && autoupdate && autoconf
	cd verilator && ./configure --prefix=$(shell realpath $(INSTALL_PREFIX))
	$(MAKE) -C verilator
	$(MAKE) -C verilator -j 1 install

clean-build:
	git submodule deinit -f verilator
	rm -rf prepare

clean: clean-build