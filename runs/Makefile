build: $(addprefix build-,$(SIMS))
clean: $(addprefix clean-,$(SIMS))

build-%:
	$(MAKE) -C $* build
clean-%:
	$(MAKE) -C $* clean