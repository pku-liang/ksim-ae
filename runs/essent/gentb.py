import sys
import re
import random

name = sys.argv[1]

print('''
#include <cstring>
#include <cstdlib>
#include <chrono>
#include "$name.h"

int main(int argc, char ** argv) {
  auto dut = new $name;
  auto cnt = atoi(argv[1]);
  dut->reset = UInt<1>(1);
  dut->eval(false, false, false);
  for (int i = 0; i < 5; i++) {
    dut->eval(true, false, false);
  }
  dut->reset = UInt<1>(0);
  dut->eval(false, false, false);
  auto start = std::chrono::system_clock::now();
  for (int i = 0; i < cnt; i++) {
'''.replace('$name', name))

vars = []

with open(name + '.h') as f:
  ioblk = False
  for line in f:
    if line.startswith(f'typedef struct {name} {{'):
      ioblk = True
    if line.startswith(f'  {name}() {{'):
      ioblk = False
    if ioblk:
      line = line.strip()
      if mat := re.fullmatch('UInt<(\d+)> ([^;]+);', line):
        width, var = mat.groups()
        if 'valid' in var.lower():
          print(f'    dut->{var} = UInt<{width}>(1);')
        elif random.randint(0, 16) == 0:
          print(f'    dut->{var} = rand() & ((1ll<<{width}) - 1);')

print('''
    dut->eval(true, false, true);
  }
  auto stop = std::chrono::system_clock::now();
  std::cout << std::chrono::duration_cast<std::chrono::microseconds>(stop - start).count() << std::endl;
  delete dut;
  return 0;
}
'''.replace('$name', name))