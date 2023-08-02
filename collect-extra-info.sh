#!/bin/bash

kernel_version() {
  echo "Arch Linux (Kernel $(uname -r))"
}

gcc_version() {
  echo -n "gcc "
  gcc --version | grep -Eo "[0-9]+\.[0-9]+\.[0-9]+"
}

llvm_version() {
  echo -n "LLVM "
  llc --version | grep -Eo "[0-9]+\.[0-9]+\.[0-9]+"
}

verilator_version() {
  echo -n "Verilator "
  verilator --version | cut -d' ' -f2
}

firrtl_version() {
  echo -n "Version: "
  if ! [ -f tools/firrtl/firrtl/build.sbt ]; then
    return 1
  fi
  cat tools/firrtl/firrtl/build.sbt | grep "  version :=" | cut -d'"' -f2
}

vcs_version() {
  vcs_version=$(basename $VCS_HOME)
  echo ${vcs_version##O-}
}

echo "field,value"
echo "OS,$(kernel_version)"
echo "Compiler,$(gcc_version) $(llvm_version)"
echo "Verilator,$(verilator_version)"
echo "FIRRTL,$(firrtl_version)"
echo "vcs,$(vcs_version)"