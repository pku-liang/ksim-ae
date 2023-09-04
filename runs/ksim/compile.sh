#!/bin/bash

design=$1
. ../common.sh
prepare_target_dir $design

# 1. run firtool to translate firrtl into circt HW dialect
firtool --ir-hw --disable-all-randomization $design.fir -o $design.mlir

# 2. ksim will generate two file:
#   * $design.ll : the compilation output, will be passed to LLVM to generate executable
#   * $design.h  : the header file, containing all the IO port defination
timeit ksim $design.mlir -v -o $design.ll --out-header=$design.h --out-driver=$design.cpp 2>&1 | tee compile.log

# 3. use llc to compile llvm code into `obj` file
llc --relocation-model=dynamic-no-pic -O2 -filetype=obj $design.ll -o $design.o

# 4. use clang to compile testbench and link `obj` file.
clang++ -O2 $design.o $design.cpp -o $design

provide_exe_file $design $design