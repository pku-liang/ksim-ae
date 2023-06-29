TARGETS=essent repcut
.phony: setup clean

setup: $(addprefix setup-,$(TARGETS))
clean: $(addprefix clean-,$(TARGETS))

setup-%:
	$(MAKE) -C $* setup
clean-%:
	$(MAKE) -C $* clean