#!/bin/bash

[ -d results ] || mkdir results

run_cycles=100000

for bench in $(cat cases.txt); do
  echo $bench
  for i in 0 1 2 3 4 5 6 7 8 9; do
    timeit --us bash -c "taskset -c 4 ./obj/$bench/simv +run=$run_cycles >/dev/null 2>/dev/null" 2>&1 | tee results/$bench.$i.txt
  done
done