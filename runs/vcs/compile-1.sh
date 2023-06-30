#!/bin/bash

design=$1
. ../common.sh
prepare_target_dir $design

top=$(sed -nE 's#circuit (.*) :#\1#p' $design.fir)
echo top module is $top
firtool $design.fir -o $design.sv
python3 $BASE_DIR/gentb.py $design.sv $top > harness.sv