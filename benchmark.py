from pathlib import Path
from perflib import run_task
import json
import os
import re

root = Path('.')
sims = re.split(r'\s+', os.environ['SIMS'].strip())
runs_dir = root.joinpath('runs')
results_dir = root.joinpath('results/runs')

num_runs = 10
run_cycle = 10000

tasksets = {
  'circt-verilator': 'taskset -c 4',
  'verilator-1': 'taskset -c 4',
  'verilator-2': 'taskset -c 4,5',
  'verilator-4': 'taskset -c 4,5,6,7',
  'ksim': 'taskset -c 4',
  'essent': 'taskset -c 4',
  'repcut-1': 'taskset -c 4',
  'repcut-2': 'taskset -c 4,5',
  'repcut-4': 'taskset -c 2,3,4,5',
  'repcut-6': 'taskset -c 0,1,2,3,4,5',
  'vcs': 'taskset -c 4'
}

benchmarks = [f.stem for f in root.joinpath('cases').glob('*.fir')]
for s in sims:
  assert s in tasksets, f"taskset command of simulator {s} is not set"

results_dir.mkdir(exist_ok=True, parents=True)
runs = [(bench, sim) for bench in benchmarks for sim in sims]
for bench, sim in runs:
  run_task(
    bench, sim, 
    exe=runs_dir.joinpath(sim, 'bin', bench + '.out'),
    taskset=tasksets[sim], 
    results_dir=results_dir,
    num_runs=num_runs,
    run_cycle=run_cycle
  )

import pandas as pd
df = []
for res in results_dir.glob('*.json'):
  with res.open() as f:
    df += json.load(f)
pd.DataFrame(df).to_csv(root.joinpath('results', 'result.csv'), index=False)