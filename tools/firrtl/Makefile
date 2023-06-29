INSTALL_DIR ?= ../bin
.phony: setup clean

setup: $(INSTALL_DIR)/firrtl
$(INSTALL_DIR)/firrtl: $(wildcard src/**/*)
	cd firrtl && sbt assembly
	cp firrtl/utils/bin/{firrtl,firrtl.jar} $(INSTALL_DIR)

clean:
	rm -rf $(INSTALL_DIR)/{firrtl, firrtl.jar}