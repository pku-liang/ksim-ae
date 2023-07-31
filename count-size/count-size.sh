#!/bin/bash

input=$1
output=$2

pipeline="builtin.module(ksim-remove-sv, ksim-flatten)"

firtool --ir-hw --disable-all-randomization -dedup $input | \
ksim --mlir-pass-statistics -o /dev/null 2> $output
