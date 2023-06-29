#!/bin/bash

design=$1
. ../common.sh
prepare_target_dir $design

firrtl -i $design.fir -o $design.v

timeit verilator --cc -DSYNTHESIS --Wno-fatal -CFLAGS "-O2" --threads 1 $design.v 2>&1 | tee compile.log
python3 $BASE_DIR/gentb.py $design > ${design}_tb.cpp
verilator --cc -DSYNTHESIS --Wno-fatal -CFLAGS "-O2" --threads 1 --exe $design.v ${design}_tb.cpp
make -C obj_dir -fV$design.mk CXXLAGS="-O2"

provide_exe_file $design obj_dir/V$design