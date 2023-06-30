import sys
import re

file = sys.argv[1]
top = sys.argv[2]

ports = []

with open(file) as f:
  start = False
  direction = 'input'
  hbit, lbit = None, None
  for line in f:
    if line.startswith(f'module {top}('):
      start = True
    elif line.startswith(');'):
      start = False
    elif start:
      line = line.strip()
      has_port_decl = False
      if line.startswith('input'):
        direction = 'input'
        line = line[len('input'):]
        has_port_decl = True
      elif line.startswith('output'):
        direction = 'output'
        line = line[len('output'):]
        has_port_decl = True
      mat = re.match(r'(?:\[(\d+):(\d+)\]\s+)?([A-Za-z0-9_]+),?', line.strip())
      if mat:
        cur_hbit, cur_lbit, name = mat.groups()
        if has_port_decl:
          hbit = cur_hbit
          lbit = cur_lbit
        ports.append((direction, hbit, lbit, name))

def make_def(hb, lb, name):
  if hb is None:
    return name
  else:
    return f'[{hb}:{lb}] {name}'

print('module harness();')

for d, hb, lb, name in ports:
  name_def = make_def(hb, lb, name)
  if d == 'input':
    print(f'  reg {name_def};')
  elif d == 'output':
    print(f'  wire {name_def};')

print(f'  {top} dut(')
print(',\n'.join(([f'    .{name}({name})' for d, hb, lb, name in ports])))
print('  );')

print('''\
  initial begin
    clock = 0;
    forever #5 clock = ~clock;
  end
  integer stop_clk;
  initial begin
    reset = 0;
    repeat(2) @(posedge clock);
    reset = 1;
    repeat(2) @(posedge clock);
    reset = 0;
    $value$plusargs("run=%d", stop_clk);
    repeat(stop_clk) @(posedge clock) begin\
''')

for d, hb, lb, name in ports:
  if d == 'input':
    print(f'      {name} <= $random();')

print('    end')

for d, hb, lb, name in ports:
  if d == 'output':
    print(f'    $display("> %d", {name});')

print('''\
    $finish();
  end
endmodule\
''')