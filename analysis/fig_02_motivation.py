from perf_data import *
from format import *
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import ticker
from scipy.stats import gmean

df = load_perf()
df['access_ratio'] = df['all_data_cache_accesses'] / df['instructions']
df = df.set_index('simulator').loc['verilator-1']
df['type'] = 'normal'
df.loc[len(df)] = pd.Series({'benchmark': 'Average', 'type': 'avg', 'access_ratio': gmean(df['access_ratio'])})
palette = sns.color_palette('muted')

plt.figure(figsize=(6, 3))
bar = sns.barplot(data=df, order=bench_order[:-1] + ['Average'], x='benchmark', y='access_ratio', errwidth=0, color=palette[0])
rect = bar.containers[0].get_children()[-1]
rect.set_facecolor(palette[1])
plt.xticks(rotation=-30, ha='left', fontsize=11)
sns.despine()
plt.xlabel(None)
plt.ylabel('Mem. Access Instructions', fontsize=14)
ax = plt.gca()
ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1))
ax.yaxis.set_major_locator(ticker.IndexLocator(0.1,0))
ax.yaxis.set_minor_locator(ticker.IndexLocator(0.05,0))
plt.grid(axis='y', alpha=0.5, which='major')
# plt.ylim([0, 1])
plt.tight_layout()
plt.savefig('out/fig_02.pdf')