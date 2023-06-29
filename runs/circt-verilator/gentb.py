import sys
import re

dut = sys.argv[1]

print(f'''#include "obj_dir/V{dut}.h"
#include <cstdlib>
#include <chrono>
#include <iostream>
double sc_time_stamp() {{ return 0; }}
int main(int argc, char ** argv) {{
  auto dut = new V{dut};
  auto cnt = atoi(argv[1]);
  dut->reset = 0;
''')

with open(f'obj_dir/V{dut}.h') as f:
  for line in f:
    line = line.strip()
    if mat := re.match("VL_(IN|OUT)\d+\(&([^,]+),([^,]+),([^,]+)\);", line):
      inout, name, h, l = mat.groups()
      value = f"rand() & ((1ull << {h}) - 1)"
      if name == "reset":
        value = 0
        print(f"  dut->{name} = {value};")
      elif "valid" in name or "vld" in name:
        value = 1
        print(f"  dut->{name} = {value};")

print(f'''
  for(int i = 0; i < cnt; i++) {{
    dut->clock = 0;
    dut->eval();
    dut->clock = 1;
    dut->eval();
  }}
''')
print(f'''
  auto start = std::chrono::system_clock::now();
  for(int i = 0; i < cnt; i++) {{
    dut->clock = 0;
    dut->eval();
    dut->clock = 1;
    dut->eval();
  }}
  auto stop = std::chrono::system_clock::now();
  std::cout << std::chrono::duration_cast<std::chrono::microseconds>(stop - start).count() << std::endl;
  return 0;
}}
''')