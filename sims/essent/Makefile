INSTALL_DIR ?= ../bin
TARGET = $(INSTALL_DIR)/essent
.phony: setup clean

.phony: setup clean

setup: $(TARGET)

$(TARGET): $(wildcard essent/src/**/*)
	cd essent && sbt assembly
	cp essent/utils/bin/* $(INSTALL_DIR)

clean:
	rm -rf $(INSTALL_DIR)/{essent,essent.jar}