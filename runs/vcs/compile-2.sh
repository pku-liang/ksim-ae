#!/bin/bash

design=$1

target_dir=obj/$design
export BASE_DIR=$PWD
set -e
pushd $target_dir

vcs -sverilog +v2k +rad -timescale=1ns/1ns -l compile.log $design.sv harness.sv -o simv