from perf_data import *
from format import *
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import ticker

df = load_perf()
df = df.set_index('benchmark').loc[bench_order].reset_index()
df['simulator'] = np.where(df['simulator'] == ours, f'{ours} (ours)', df['simulator'])
sim_order[sim_order.index(ours)] = f'{ours} (ours)'
df['access-per-cycle'] = df['all_data_cache_accesses'] / df['sim-cycles']
df['speed'] = df['sim-cycles'] / df['time']

piv = df.pivot_table(values='access-per-cycle', index='benchmark', columns='simulator')
red = (piv['circt-verilator'] - piv[f'{ours} (ours)']) / (piv['circt-verilator'])

plt.figure(figsize=large_fig_size)
bar = sns.barplot(
  data=df,
  x='benchmark', y='access-per-cycle',
  hue='simulator', hue_order=sim_order,
  palette='muted',
  width=bar_width
)
plt.ylim([1e2, 1e7])
plt.yscale('log')
mark_npos(bar, 0.05, 'rx', markersize=8, label='compiler crash')
plt.xticks(fontsize=13)
plt.xlabel(None)
plt.ylabel('Memory Accesses', fontsize=14)
handles, labels = plt.gca().get_legend_handles_labels()
plt.legend(handles[1:] + handles[:1], labels[1:] + labels[:1], loc='upper right', ncol=4)
sns.despine()
plt.gca().yaxis.set_major_locator(ticker.LogLocator(base=10, subs=(1,), numticks=100))
plt.gca().yaxis.set_minor_locator(ticker.LogLocator(base=10, subs=(2,4,6,8), numticks=100))
plt.grid(axis='y', which='major', alpha=0.5)
plt.subplots_adjust(left=0.05, right=0.97, bottom=0.13, top=0.95)
plt.savefig('out/fig_10_1.pdf')