from pathlib import Path
import subprocess
import json
import re
import os

root = Path('.')
sims = re.split(r'\s+', os.environ['SIMS'].strip())
benchmarks = [f.stem for f in root.joinpath('cases').glob('*.fir')]

df = []

for bench in benchmarks:
  for sim in sims:
    log_path = Path('runs', sim, 'obj', bench, 'compile.log')
    if not log_path.exists(): continue
    data = log_path.read_text()
    if mat := re.search('Wall Time: (\d+)\n', data):
      tm = mat.group(1)
      df.append({
        'benchmark': bench,
        'simulator': sim,
        'comp_time': tm
      })
    else:
      print(bench, sim)

import pandas as pd
pd.DataFrame(df).to_csv('results/comp-time.csv', index=False)