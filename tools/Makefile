TARGETS=timeit firclean firrtl

setup: $(addprefix setup-,$(TARGETS))
clean: $(addprefix clean-,$(TARGETS))

setup-%:
	$(MAKE) -C $* setup
clean-%:
	$(MAKE) -C $* clean