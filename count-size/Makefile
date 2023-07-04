CASE_ROOT = $(TEST_ROOT)/cases
CASES = $(wildcard $(CASE_ROOT)/*.fir)
TARGETS = $(patsubst $(CASE_ROOT)/%.fir,obj/%.txt,$(CASES))
$(shell [ -d obj ] || mkdir obj)

all: $(TARGETS)

obj/%.txt: $(wildcard $(CASE_ROOT)/*.fir)
	./count-size.sh $^ $@