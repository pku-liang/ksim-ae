CASE_ROOT = $(TEST_ROOT)/cases
ALL_CASES := $(patsubst $(CASE_ROOT)/%.fir,%,$(wildcard $(CASE_ROOT)/*.fir))
CASES := $(filter-out $(FILTER_OUT_CASE), $(ALL_CASES))

.phony: step1 step2

build: step1

step1: $(patsubst %,obj/%/harness.sv,$(CASES))
	@echo $(CASES) > cases.txt
	rsync -avz * eda:ksim-test/runs/vcs/
	rsync -avz $(TEST_ROOT)/tools/timeit eda:ksim-test/tools/

SAVED_CASES=$(shell [ -f cases.txt ] && cat cases.txt)
step2: $(patsubst %,obj/%/simv,$(SAVED_CASES))
	./perf.sh

step3:
	rsync -avz eda:ksim-test/runs/vcs/results ./

obj/%/harness.sv: $(CASE_ROOT)/%.fir $(EXTRA_DEPEND)
	./compile-1.sh $* || rm -rf $@

obj/%/simv: obj/%/harness.sv
	./compile-2.sh $*

clean:
	rm -rf bin obj