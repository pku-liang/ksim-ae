#!/bin/bash

set -xe

input=$1
output=$2

firtool --ir-hw --disable-all-randomization -dedup $input | \
ksim --compute-fused -o /dev/null 2>$output
