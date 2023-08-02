.phony: build clean-build run clean-run

define assert_env
@if [ -z $${_KSIM_AE_PATH_UPDATED+x} ]; then tput setaf 1; echo "Please source env.sh first!"; tput setaf 7; exit 1; fi
endef

build:
	$(assert_env)
	$(MAKE) -C runs build
clean-build:
	$(assert_env)
	$(MAKE) -C runs clean

run-all: run results/cpu-info.json results/size.csv results/extra-info.csv

run:
	$(assert_env)
	python benchmark.py
clean-run:
	$(assert_env)
	rm -rf results

results/extra-info.csv:
	$(assert_env)
	./collect-extra-info.sh > $@
results/cpu-info.json:
	$(assert_env)
	lscpu -J > $@
results/size.csv:
	$(assert_env)
	$(MAKE) -C count-size

report:
	$(assert_env)
	$(MAKE) -j -C analysis/data
	$(MAKE) -j -C analysis
	cp analysis/report/report.pdf ./
	@tput setaf 2; echo "Finish, see report.pdf to verify the artifact"; tput setaf 7

.phony: prepare-setup setup distclean

prepare-setup: prepare-setup-sims prepare-setup-tools
prepare-setup-%:
	$(MAKE) -C $* prepare

setup: setup-sims setup-tools
setup-%:
	$(MAKE) -C $* setup

distclean:
	$(MAKE) -C count-fuse clean
	$(MAKE) -C count-size clean
	$(MAKE) -C runs clean
	$(MAKE) -C sims clean
	$(MAKE) -C tools clean
	$(MAKE) -C analysis clean
	$(MAKE) -C analysis/data clean