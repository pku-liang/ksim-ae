export TEST_ROOT=$PWD
export HOSTS="base plat-1 plat-2"
export SIMS="circt-verilator verilator-1 verilator-2 verilator-4 ksim essent repcut-1 repcut-2 repcut-4 repcut-6 repcut-8"
if [[ "$_KSIM_AE_PATH_UPDATED" != "1" ]]; then
  export PATH=$TEST_ROOT/sims/bin:$TEST_ROOT/sims/install/bin:$TEST_ROOT/tools/bin:$PATH
fi
if which vcs >/dev/null 2>/dev/null; then
  export SIMS="$SIMS vcs"
fi
export _KSIM_AE_PATH_UPDATED=1

_color_print() {
  tput setaf "$1"
  printf "%s     \t" "$2"
  tput setaf 7
  printf "%s\n" "$3"
}

_show_status() {
  if ! which $1 2>/dev/null > /dev/null; then
    _color_print 1 "$1" "is not found"
    return 1
  else
    show_path=$(which $1)
    if realpath --relative-to=$PWD $show_path 2>/dev/null >/dev/null; then
      new_show_path=./$(realpath --relative-to=$PWD $show_path)
      if [ ${#new_show_path} -le ${#show_path} ]; then
        show_path=$new_show_path
      fi
    fi
    _color_print 2 "$1" "is at $show_path"
    return 0
  fi
}

_show_ssh() {
  if ! ssh $1 true; then
    _color_print 1 "$1" "unable to connect"
    return 1
  else
    _color_print 2 "$1" "success to connect"
    return 0
  fi
}

show-status() {
  echo "Check Tools"
  tools="ksim llc verilator firtool firrtl g++ clang++ essent repcut KaHyPar firclean timeit vcs"
  for tool in $(echo $tools); do
    _show_status $tool
  done
  echo
  _color_print 4 "Runs:" "$SIMS"
  echo
  echo "Check SSH Connectivity"
  for plat in $(echo $HOSTS); do
    _show_ssh $plat
  done
}

show-status
