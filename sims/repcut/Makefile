INSTALL_DIR ?= ../bin
.phony: setup clean

setup: $(INSTALL_DIR)/repcut $(INSTALL_DIR)/KaHyPar

prepare-kahypar: kahypar.patch
	git submodule deinit -f kahypar; git submodule update --init kahypar
	cd kahypar && git apply ../kahypar.patch
	touch $@
prepare-repcut: repcut.patch
	git submodule deinit -f essent; git submodule update --init essent
	cd essent && git apply ../repcut.patch
	touch $@

$(INSTALL_DIR)/repcut: prepare-repcut $(wildcard essent/src/**/*)
	cd essent && sbt assembly
	cp essent/utils/bin/essent.jar $(INSTALL_DIR)/repcut.jar
	sed -e 's/essent.jar/repcut.jar/g' essent/utils/bin/essent > $(INSTALL_DIR)/repcut
	chmod +x $(INSTALL_DIR)/repcut

$(INSTALL_DIR)/KaHyPar: prepare-kahypar $(wildcard kahypar/kahypar/**/*)
	./setup-kahypar.sh
	$(MAKE) -C kahypar/build
	cp kahypar/build/kahypar/application/KaHyPar $@

clean:
	rm -rf $(INSTALL_DIR)/{repcut, repcut.jar, KaHyPar}