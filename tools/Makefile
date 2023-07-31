$(shell [ -d bin ] || mkdir bin)
TARGETS=timeit firclean firrtl

prepare: $(addprefix prepare-,$(TARGETS))
setup: $(addprefix setup-,$(TARGETS))
clean: $(addprefix clean-,$(TARGETS))

prepare-%:
	$(MAKE) -C $* prepare
setup-%:
	$(MAKE) -C $* setup
clean-%:
	$(MAKE) -C $* clean