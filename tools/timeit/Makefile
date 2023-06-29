INSTALL_DIR ?= ../bin
.phony: setup clean

setup: $(INSTALL_DIR)/timeit
$(INSTALL_DIR)/timeit: timeit.cpp
	g++ -O2 $< -o $@

clean:
	rm -rf $(INSTALL_DIR)/timeit