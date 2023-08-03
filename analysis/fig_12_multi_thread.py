from perf_data import *
from format import *
import pandas as pd
import numpy as np
import seaborn as sns
from scipy.stats import gmean
import matplotlib.pyplot as plt
from matplotlib import ticker

df = load_perf(order=mt_order)
df = df[df.run >= 3].copy()
df['speed'] = df['sim-cycles'] / df['time']
df['ipc'] = df['instructions'] / df['cycles']
# df['MPKI'] = df['cache-misses'] / df['instructions'] * 1000

piv = df.pivot_table(values='speed', index='benchmark', columns='simulator')
baseline = piv[baseline_name].copy()
for col in piv:
  piv[col] /= baseline
piv = piv.stack().reset_index(name='speedup')

plt.figure(figsize=large_fig_size)
bar = sns.barplot(
  data=piv,
  x='benchmark', y='speedup',
  hue='simulator', hue_order=mt_order,
  palette=mt_color,
  width=1 - 1 / (len(sim_order) + 1),
)

mark_npos(bar, 0.05, 'rx', markersize=8, label='compiler crash')
handles, labels = plt.gca().get_legend_handles_labels()
plt.legend(handles[1:] + handles[:1], labels[1:] + labels[:1], loc='upper right', ncol=5, frameon=False)
plt.xticks(fontsize=13)
plt.xlabel(None)
plt.ylabel('Speedup', fontsize=14)
ax = plt.gca()
ax.yaxis.set_major_locator(ticker.IndexLocator(base=1, offset=0))
ax.yaxis.set_minor_locator(ticker.IndexLocator(base=0.5, offset=0))
plt.grid(axis='y', alpha=0.3)
plt.grid(axis='y', which='minor', alpha=0.3)
sns.despine()
plt.subplots_adjust(left=0.05, right=0.97, bottom=0.2, top=0.97)
plt.savefig('out/fig_12.pdf')