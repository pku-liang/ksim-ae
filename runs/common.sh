#!/bin/bash

# TEST_ROOT: 

prepare_target_dir() {
  design=$1
  target_dir=obj/$design
  [ -d bin ] || mkdir bin
  [ -d $target_dir ] || rm -rf $target_dir
  mkdir -p $target_dir
  cp $TEST_ROOT/cases/$design.fir $target_dir/$design.fir
  export BASE_DIR=$PWD
  set -e
  pushd $target_dir
}

enter_target_dir() {
  design=$1
  target_dir=obj/$design
  export BASE_DIR=$PWD
  set -e
  pushd $target_dir
}

provide_exe_file() {
  design=$1
  file=$2
  cp $file $BASE_DIR/bin/$design.out
}
