#!/bin/bash

design=$1
. ../common.sh
prepare_target_dir $design

firtool --ir-hw --disable-all-randomization $design.fir -o $design.mlir
timeit ksim $design.mlir -v -o $design.ll --out-header=$design.h --out-driver=$design.cpp 2>&1 | tee compile.log
llc --relocation-model=dynamic-no-pic -O2 -filetype=obj $design.ll -o $design.o
clang++ -O2 $design.o $design.cpp -o $design

provide_exe_file $design $design