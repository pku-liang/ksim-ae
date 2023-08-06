INSTALL_DIR ?= ../bin
.phony: setup clean

setup: $(INSTALL_DIR)/firrtl

prepare:
	git submodule deinit -f firrtl; git submodule update --init firrtl
	touch $@

$(INSTALL_DIR)/firrtl: prepare $(wildcard src/**/*)
	cd firrtl && sbt assembly
	cp firrtl/utils/bin/{firrtl,firrtl.jar} $(INSTALL_DIR)

clean-build:
	git submodule deinit -f firrtl
	rm -rf prepare

clean: clean-build
	rm -rf $(INSTALL_DIR)/{firrtl,firrtl.jar}