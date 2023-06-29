INSTALL_DIR ?= ../bin
.phony: setup clean

setup: $(INSTALL_DIR)/repcut $(INSTALL_DIR)/KaHyPar

prepare: kahypar.patch
	cd kahypar && git apply ../kahypar.patch
	touch prepare

$(INSTALL_DIR)/repcut: $(wildcard essent/src/**/*)
	cd essent && sbt assembly
	cp essent/utils/bin/essent.jar $(INSTALL_DIR)/repcut.jar
	sed -e 's/essent.jar/repcut.jar/g' essent/utils/bin/essent > $(INSTALL_DIR)/repcut
	chmod +x $(INSTALL_DIR)/repcut

$(INSTALL_DIR)/KaHyPar: prepare $(wildcard kahypar/kahypar/**/*)
	./setup-kahypar.sh
	$(MAKE) -C kahypar/build
	cp kahypar/build/kahypar/application/KaHyPar $@

clean:
	rm -rf $(INSTALL_DIR)/{repcut, repcut.jar, KaHyPar}