#!/bin/bash

design=$1
. ../common.sh
prepare_target_dir $design

# 1. remove print, assert and other special operations
firclean $design.fir $design.cleaned.fir

# 2. essent will compile firrtl into a cpp file
timeit essent ./$design.cleaned.fir -O3 2>&1 | tee compile.log

# 3. read the generated cpp file to generate testbench
top=$(find . -name "*.h")
top=${top//.\//}
top=${top%%.h}
python3 $BASE_DIR/gentb.py $top > ${design}_tb.cpp

# 4. compile all together
ccache g++ -O2 ${design}_tb.cpp -I$TEST_ROOT/sims/include -o $design

provide_exe_file $design $design