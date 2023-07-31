TARGETS=essent repcut verilator ksim
.phony: setup clean

setup: $(addprefix setup-,$(TARGETS))
cleanbuild: $(addprefix cleanbuild-,$(TARGETS))
clean: $(addprefix clean-,$(TARGETS))
	rm -rf install bin

setup-%:
	$(MAKE) -C $* setup
cleanbuild-%:
	$(MAKE) -C $* clean-build
clean-%:
	$(MAKE) -C $* clean