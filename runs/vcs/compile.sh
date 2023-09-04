#!/bin/bash

design=$1
. ../common.sh
prepare_target_dir $design

# 1. find top module in the circuit
top=$(sed -nE 's#circuit (.*) :#\1#p' $design.fir)
echo top module is $top

# 2. firrtl to sv
firtool $design.fir -o $design.sv

# 3. generate testbench
python3 $BASE_DIR/gentb.py $design.sv $top > harness.sv

# 4. use vcs to compile all sources
timeit vcs -full64 -sverilog +v2k -q -timescale=1ns/1ns -l compile.log $design.sv harness.sv -o simv 2>&1 | tee compile.log

# 5. create a wrapper to simulate specific cycles
cat >run.sh <<EOF
#!/bin/bash
timeit --us bash -c "$PWD/simv +run=\$1 >/dev/null 2>/dev/null"
EOF
chmod +x ./run.sh

provide_exe_file $design ./run.sh