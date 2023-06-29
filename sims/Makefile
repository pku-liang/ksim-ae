TARGETS=essent repcut
.phony: setup clean

setup: $(addprefix setup-,$(TARGETS))
cleanbuild: $(addprefix cleanbuild-,$(TARGETS))
clean: $(addprefix clean-,$(TARGETS))

setup-%:
	$(MAKE) -C $* setup
cleanbuild-%:
	$(MAKE) -C $* clean-build
clean-%:
	$(MAKE) -C $* clean