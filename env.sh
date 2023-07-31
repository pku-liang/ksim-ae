export TEST_ROOT=$PWD
export PATH=$TEST_ROOT/sims/bin:$TEST_ROOT/sims/install/bin:$TEST_ROOT/tools/bin:$PATH
export SIMS="circt-verilator verilator-1 verilator-2 verilator-4 ksim essent repcut-1 repcut-2 repcut-4 repcut-6 repcut-8 vcs"

_show_status() {
  if ! which $1 2&>1 > /dev/null; then
    tput setaf 1
    printf "%s     \t" $1
    tput setaf 7
    printf "is not found\n" $1
  else
    tput setaf 2
    printf "%s     \t" $1
    tput setaf 7
    show_path=$(which $1)
    if realpath --relative-to=$PWD $show_path 2&>1 >/dev/null; then
      show_path=$(realpath --relative-to=$PWD $show_path)
    fi
    printf "is at %s\n" "$show_path"
  fi
}

show-status() {
  _show_status ksim
  _show_status llc
  _show_status verilator
  _show_status firtool
  _show_status firrtl
  _show_status g++
  _show_status clang++
  _show_status essent
  _show_status repcut
  _show_status KaHyPar
  _show_status firclean
  _show_status timeit
  _show_status vcs
}

show-status
