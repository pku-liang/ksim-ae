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
    dut->eval(true, false, true);
  }
  auto stop = std::chrono::system_clock::now();
  std::cout << std::chrono::duration_cast<std::chrono::microseconds>(stop - start).count() << std::endl;
  delete dut;
  return 0;
}
