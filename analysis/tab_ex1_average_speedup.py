from perf_data import *
from format import *
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import ticker

speedups = []

for plat in plats:
  df = load_perf(f'data/{plat}/result.csv')
  df['speed'] = df['sim-cycles'] / df['time']
  piv = df.pivot_table(values='speed', index='benchmark', columns='simulator')
  baseline = piv[baseline_name].copy()
  for col in piv: piv[col] /= baseline
  speedups.append(piv.mean())

df = pd.DataFrame(speedups, index=plats).T
df.index.name = None
s = df.style
s.set_table_styles([{'selector': '', 'props': ':small'}])
s.format('{:.2f}', na_rep='-').to_latex(
  'out/tab_ex1.tex',
  caption='Average Speedup',
  hrules=True,
  position_float='centering',
  label='tab:avg-speedup'
)