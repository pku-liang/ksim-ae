export TEST_ROOT=$PWD
export PATH=$TEST_ROOT/sims/bin:$TEST_ROOT/sims/install/bin:$TEST_ROOT/tools/bin:$PATH
export SIMS="verilator ksim repcut-2 circt-verilator essent"

_show_status() {
  if ! which $1 > /dev/null; then
    tput setaf 1
    printf "%s     \tis not found\n" $1
  else
    tput setaf 2
    printf "%s     \tis at %s\n" $1 $(which $1)
  fi
  tput setaf 7
}

env-status() {
  _show_status ksim
  _show_status llc
  _show_status verilator
  _show_status firtool
  _show_status firrtl
  _show_status essent
  _show_status repcut
  _show_status KaHyPar
  _show_status firclean
  _show_status timeit
}