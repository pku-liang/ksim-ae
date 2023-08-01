from perf_data import *
from format import *
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import ticker

def plot(df: pd.DataFrame, set_ours=True):
  df = df.set_index('benchmark').loc[bench_order].reset_index()
  if set_ours:
    df['simulator'] = np.where(df['simulator'] == ours, f'{ours} (ours)', df['simulator'])
    sim_order[sim_order.index(ours)] = f'{ours} (ours)'
  df['speed'] = df['sim-cycles'] / df['time']

  piv = df.pivot_table(values='speed', index='benchmark', columns='simulator')
  baseline = piv[baseline_name].copy()
  for col in piv: piv[col] /= baseline
  piv = piv.stack().reset_index(name='speedup')

  plt.figure(figsize=large_fig_size)
  bar = sns.barplot(
    data=piv, order=bench_order,
    x='benchmark', y='speedup',
    hue='simulator', hue_order=sim_order,
    palette='muted',
    width=bar_width,
  )
  mark_npos(bar, 0.05, 'rx', markersize=8, label='compiler crash')
  handles, labels = plt.gca().get_legend_handles_labels()
  plt.legend(handles[1:] + handles[:1], labels[1:] + labels[:1], loc='upper right', ncol=4)
  plt.xticks(fontsize=13)
  plt.xlabel(None)
  plt.ylabel('Speedup', fontsize=14)
  ax = plt.gca()
  ax.yaxis.set_major_locator(ticker.IndexLocator(base=0.5, offset=0))
  ax.yaxis.set_minor_locator(ticker.IndexLocator(base=0.25, offset=0))
  plt.grid(axis='y', alpha=0.3)
  sns.despine()
  plt.subplots_adjust(left=0.05, right=0.97, bottom=0.13, top=0.95)

if __name__ == '__main__':
  plot(load_perf())
  plt.savefig('out/fig_10_2.pdf')