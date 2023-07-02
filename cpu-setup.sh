#!/bin/bash

freq=2200000

echo available frequencies:
cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_available_frequencies

echo $freq | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_max_freq > /dev/null
echo $freq | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_min_freq > /dev/null
echo 0 | tee /sys/devices/system/cpu/cpufreq/boost > /dev/null

echo "current frequencies:"
cd /sys/devices/system/cpu/
for cpu in cpu*/cpufreq; do
  printf "%s\t%s\n" "$cpu" "$(cat $cpu/scaling_cur_freq)"
done
