#!/bin/bash

design=$1
. ../common.sh
prepare_target_dir $design

# 1. generate verilog
firrtl -i $design.fir -o $design.v

# 2. use verilator to generate targets
#    here, -DSYNTHESIS is used, to disable randomization
timeit verilator --cc -DSYNTHESIS --Wno-fatal -CFLAGS "-O2" --threads 1 $design.v 2>&1 | tee compile.log

# 3. read the generated file and generate testbench
python3 $BASE_DIR/gentb.py $design > ${design}_tb.cpp

# 4. add testbench to the source list, add `--exe` to generate an executable file
verilator --cc -DSYNTHESIS --Wno-fatal -CFLAGS "-O2" --threads 1 --exe $design.v ${design}_tb.cpp

# 5. run make to compile the generated file
make -C obj_dir -fV$design.mk CXXLAGS="-O2"

provide_exe_file $design obj_dir/V$design