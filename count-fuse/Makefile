CASE_ROOT = $(TEST_ROOT)/cases
CASES = $(wildcard $(CASE_ROOT)/*.fir)
TARGETS = $(patsubst $(CASE_ROOT)/%.fir,obj/%.txt,$(CASES))
EXTRA_DEP = $(shell which ksim) count-fuse.sh
$(shell [ -d obj ] || mkdir obj)

all: $(TARGETS) $(CASE_ROOT)/results/fused.csv
run: $(TARGETS)

$(CASE_ROOT)/results/fused.csv: collect.py $(TARGETS)
	python collect.py

obj/%.txt: $(CASE_ROOT)/%.fir $(EXTRA_DEP)
	./count-fuse.sh $< $@

clean:
	rm -rf obj