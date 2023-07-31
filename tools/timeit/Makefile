INSTALL_DIR ?= ../bin
.phony: setup clean

prepare:

setup: $(INSTALL_DIR)/timeit
$(INSTALL_DIR)/timeit: timeit.cpp
	g++ -std=c++11 -O2 $< -o $@

clean:
	rm -rf $(INSTALL_DIR)/timeit