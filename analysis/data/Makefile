collect: $(addprefix collect-,$(HOSTS))

collect-%:
	[ -d $* ] || mkdir $*
	rsync -au --exclude=runs $*:ksim-ae/results/ ./$*/

clean:
	rm -rf $(HOSTS)