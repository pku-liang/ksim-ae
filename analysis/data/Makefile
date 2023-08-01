collect: $(addprefix collect-,$(HOSTS))

collect-%:
	[ -d $* ] || mkdir $*
	rsync -au --exclude=runs $*:ksim-ae/results/ ./$*/
	touch -m $*

clean:
	rm -rf $(HOSTS)