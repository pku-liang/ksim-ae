from perf_data import *
from format import *
from pandas.io.formats.style import Styler
import pandas as pd
from pathlib import Path


def format_large(x):
  units = ['', 'k', 'M', 'G', 'T', 'E']
  for u in units:
    if x < 1: return f'{x:.2f}{u}'
    if x < 100: return f'{x:.1f}{u}'
    x /= 1000

def make_latex_table(tab: pd.DataFrame) -> Styler:
  tab.index.name = None
  tab = tab.style
  # tab = tab.set_table_styles([
  #     {'selector': 'toprule', 'props': ':hline;'},
  #     {'selector': 'midrule', 'props': ':hline;'},
  #     {'selector': 'bottomrule', 'props': ':hline;'}
  # ], overwrite=True)#.hide(axis='index')
  tab.set_table_styles([{'selector': '', 'props': ':small'}])
  tab = tab.applymap_index(lambda x: 'textbf:--rwrap', 1)
  return tab

def export_latex(tab_s):
  return tab_s.to_latex().split('\hline')[2].strip()[:-2].strip()

def make_table(df: pd.DataFrame, field='OPS') -> Styler:
  df = df.set_index('simulator').loc[sim_order].reset_index()
  df['IPC'] = df['instructions'] / df['cycles']
  df['OPS'] = df['instructions'] / 1000000000
  piv = df.pivot_table(field, index='benchmark', columns='simulator')[sim_order].loc[bench_order]
  piv.columns = ['C-Ver', 'Ver-1', 'Khr', 'ESS', 'Rep-1', 'VCS']
  piv_s = make_latex_table(piv)
  piv_s = piv_s.format('{:.2f}', na_rep='-')
  piv_s = piv_s.highlight_min(axis=1, color='green', props='textbf:--rwrap')
  return piv_s

if __name__ == '__main__':
  make_table(load_perf(), 'IPC').to_latex(
    'out/tab_09.tex', 
    caption='Instructions Per Cycle',
    position_float="centering",
    hrules=True
  )