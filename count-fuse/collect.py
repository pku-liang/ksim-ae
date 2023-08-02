from pathlib import Path
import os
import re

df = []

for file in Path('./obj').glob('*.txt'):
  data = re.findall()

cases = Path(os.environ['TEST_ROOT']).joinpath('cases')
cases = [f.stem for f in cases.glob('*.fir')]
obj_dir = Path('obj')

for case in cases:
  data = obj_dir.joinpath(case, 'compile.log').read_text()
  init_cost = 0
  min_cost = 1e9
  for it, cost in re.findall(r'It: (\d+) Cost: (\d+)', data):
    it, cost = map(int, (it, cost))
    if it == 0: init_cost = cost
    if cost < min_cost: min_cost = cost
  print(case, min_cost, init_cost)