#!/bin/bash

input=$1
output=$2

pipeline="builtin.module(ksim-remove-sv, ksim-flatten)"

echo $output

firtool --ir-hw --disable-all-randomization -dedup $input | \
ksim-opt --pass-pipeline="$pipeline" --mlir-pass-statistics -o /dev/null
