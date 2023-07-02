INSTALL_DIR ?= ../bin
TARGET = $(INSTALL_DIR)/essent
.phony: setup clean clean-build

setup: $(TARGET)

prepare: essent.patch
	git submodule deinit -f essent; git submodule update --init essent
	cd essent && git apply ../essent.patch
	touch prepare

$(TARGET): prepare $(wildcard essent/src/**/*)
	cd essent && sbt assembly
	cp essent/utils/bin/* $(INSTALL_DIR)

clean-build:
	git submodule deinit -f essent
	rm -rf prepare*

clean:
	rm -rf $(INSTALL_DIR)/{essent,essent.jar}