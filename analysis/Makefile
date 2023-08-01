$(shell [ -d out ] || mkdir out)
all_data=$(wildcard data/*) $(wildcard data/**/*)
targets=tab_05.tex tab_07_1.tex tab_07_2.tex tab_09.tex tab_10.tex \
	fig_10_1.pdf fig_10_2.pdf fig_12.pdf fig_13_1.pdf fig_13_2.pdf \
	tab_ex1.tex

all: $(addprefix out/,$(targets))
	$(MAKE) -C report

define add_dep
out/$1: $(wildcard $(basename $1)_*.py) $(all_data)
	python $$<

endef

$(eval $(foreach T,$(targets),$(call add_dep,$(T))))

clean:
	$(MAKE) -C report clean
	rm -rf out