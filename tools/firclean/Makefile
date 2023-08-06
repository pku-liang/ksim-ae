INSTALL_DIR ?= ../bin
.phony: setup clean

prepare:

setup: $(INSTALL_DIR)/firclean
$(INSTALL_DIR)/firclean: firclean.jar firclean
	cp $^ $(INSTALL_DIR)

firclean.jar: $(wildcard src/**/*)
	sbt assembly

clean:
	rm -rf $(INSTALL_DIR)/{firclean,firclean.jar}
	rm -rf target firclean.jar project/target project/project/target