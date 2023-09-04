#!/bin/bash

design=$1
. ../common.sh
prepare_target_dir $design

# 1. remove print, assert and other special operations
firclean $design.fir $design.cleaned.fir

# 2. repcut will compile firrtl into a cpp file
timeit repcut ./$design.cleaned.fir -O0 --parallel 4 2>&1 | tee compile.log

# 3. read the generated cpp file to generate testbench
top=$(find . -name "*.h")
top=${top//.\//}
top=${top%%.h}
env name=$top envsubst < $BASE_DIR/tb_template.cpp > ${design}_tb.cpp

# 4. compile all together
g++ -O2 ${design}_tb.cpp -I$TEST_ROOT/sims/include -o $design

provide_exe_file $design $design