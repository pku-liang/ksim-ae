CASE_ROOT = $(TEST_ROOT)/cases
ALL_CASES := $(patsubst $(CASE_ROOT)/%.fir,%,$(wildcard $(CASE_ROOT)/*.fir))
CASES := $(filter-out $(FILTER_OUT_CASE), $(ALL_CASES))
COMPILE_SCRIPT ?= compile.sh

.phony: build clean show-fail

$(shell [ -d bin ] || mkdir bin)
$(shell [ -d obj ] || mkdir obj)
build: $(patsubst %,bin/%.out,$(CASES))

bin/%.out: $(CASE_ROOT)/%.fir $(EXTRA_DEPEND)
	./$(COMPILE_SCRIPT) $* || touch bin/$*.fail 

clean:
	rm -rf bin obj