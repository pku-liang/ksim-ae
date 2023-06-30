CASE_ROOT = $(TEST_ROOT)/cases

.phony: build clean show-fail

$(shell [ -d bin ] || mkdir bin)
$(shell [ -d obj ] || mkdir obj)
build: $(patsubst $(CASE_ROOT)/%.fir,bin/%.out,$(wildcard $(CASE_ROOT)/*.fir))

bin/%.out: $(CASE_ROOT)/%.fir $(EXTRA_DEPEND)
	./compile.sh $* || touch bin/$*.fail 

clean:
	rm -rf bin obj