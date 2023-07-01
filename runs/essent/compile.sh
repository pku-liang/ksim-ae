#!/bin/bash

design=$1
. ../common.sh
prepare_target_dir $design

firclean $design.fir $design.cleaned.fir
timeit essent ./$design.cleaned.fir -O3 2>&1 | tee compile.log

top=$(find . -name "*.h")
top=${top//.\//}
top=${top%%.h}
python3 $BASE_DIR/gentb.py $top > ${design}_tb.cpp

g++ -O2 ${design}_tb.cpp -I$TEST_ROOT/sims/include -o $design

provide_exe_file $design $design