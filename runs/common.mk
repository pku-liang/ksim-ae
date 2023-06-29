CASE_ROOT = $(TEST_ROOT)/cases

build: $(patsubst $(CASE_ROOT)/%.fir,bin/%.out,$(wildcard $(CASE_ROOT)/*.fir))

bin/%.out: $(CASE_ROOT)/%.fir $(EXTRA_DEPEND)
	./compile.sh $*

clean:
	rm -rf bin obj