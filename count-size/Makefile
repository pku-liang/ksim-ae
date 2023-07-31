CASE_ROOT = $(TEST_ROOT)/cases
CASES = $(wildcard $(CASE_ROOT)/*.fir)
TARGETS = $(patsubst $(CASE_ROOT)/%.fir,obj/%.txt,$(CASES))
EXTRA_DEP = $(shell which ksim)
$(shell [ -d obj ] || mkdir obj)

all: $(TARGETS) $(CASE_ROOT)/results/size.csv

$(CASE_ROOT)/results/size.csv: collect.py $(TARGETS)
	python collect.py

obj/%.txt: $(CASE_ROOT)/%.fir $(EXTRA_DEP)
	./count-size.sh $< $@