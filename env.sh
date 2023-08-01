export TEST_ROOT=$PWD
export HOSTS="plat-2 plat-3"
export SIMS="circt-verilator verilator-1 verilator-2 verilator-4 ksim essent repcut-1 repcut-2 repcut-4 repcut-6 repcut-8"
if [[ "$_KSIM_AE_PATH_UPDATED" != "1" ]]; then
  export PATH=$TEST_ROOT/sims/bin:$TEST_ROOT/sims/install/bin:$TEST_ROOT/tools/bin:$PATH
fi
if which vcs >/dev/null 2>/dev/null; then
  export SIMS="$SIMS vcs"
fi
export _KSIM_AE_PATH_UPDATED=1

_color_print() {
  tput setaf $1
  printf "%s     \t" $2
  tput setaf 7
  printf "%s\n" $3
}

_show_status() {
  if ! which $1 2>/dev/null > /dev/null; then
    _color_print 1 "$1" "is not found"
  else
    show_path=$(which $1)
    if realpath --relative-to=$PWD $show_path 2>/dev/null >/dev/null; then
      new_show_path=./$(realpath --relative-to=$PWD $show_path)
      if [ ${#new_show_path} -le ${#show_path} ]; then
        show_path=$new_show_path
      fi
    fi
    _color_print 2 "$1" "is at $show_path"
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
  echo
  _color_print 4 "runs:" "$SIMS"
  _color_print 4 "hosts:" "$HOSTS"
}

show-status
