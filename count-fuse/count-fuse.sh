#!/bin/bash

set -xe

input=$1
output=$2

# run ksim with statistics
firtool --ir-hw --disable-all-randomization -dedup $input | \
ksim -v --compute-fused -o /dev/null 2>$output
