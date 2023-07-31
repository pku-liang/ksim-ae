$(shell [ -d bin ] || mkdir bin)

TARGETS=essent repcut verilator ksim
.phony: setup clean

prepare: $(addprefix prepare-,$(TARGETS))
setup: $(addprefix setup-,$(TARGETS))
cleanbuild: $(addprefix cleanbuild-,$(TARGETS))
clean: $(addprefix clean-,$(TARGETS))
	rm -rf install bin

prepare-%:
	$(MAKE) -C $* prepare
setup-%:
	$(MAKE) -C $* setup
cleanbuild-%:
	$(MAKE) -C $* clean-build
clean-%:
	$(MAKE) -C $* clean