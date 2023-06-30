#!/bin/bash

design=$1
. ../common.sh
prepare_target_dir $design

firclean $design.fir $design.cleaned.fir
timeit repcut ./$design.cleaned.fir -O0 --parallel 2 2>&1 | tee compile.log

top=$(find . -name "*.h")
top=${top//.\//}
top=${top%%.h}
env name=$top envsubst < $BASE_DIR/tb_template.cpp > ${design}_tb.cpp

g++ -O2 ${design}_tb.cpp -I$TEST_ROOT/sims/include -o $design

provide_exe_file $design $design