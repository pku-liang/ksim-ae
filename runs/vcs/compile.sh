#!/bin/bash

design=$1
. ../common.sh
prepare_target_dir $design


top=$(sed -nE 's#circuit (.*) :#\1#p' $design.fir)
echo top module is $top
firtool $design.fir -o $design.sv
python3 $BASE_DIR/gentb.py $design.sv $top > harness.sv

timeit vcs -sverilog +v2k +rad -q -timescale=1ns/1ns -l compile.log $design.sv harness.sv -o simv 2>&1 | tee compile.log

cat >run.sh <<EOF
#!/bin/bash
timeit --us bash -c "$PWD/simv +run=\$1 >/dev/null 2>/dev/null"
EOF
chmod +x ./run.sh

provide_exe_file $design ./run.sh