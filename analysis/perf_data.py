import numpy as np
import pandas as pd
import seaborn as sns
from common import *
from typing import List

rename_benchmark = {}
baseline_name = 'circt-verilator'
ours = 'khronos'

rename_simulator = {'ksim': 'khronos'}
sim_order = ['circt-verilator', 'verilator-1', 'khronos', 'essent', 'repcut-1', 'vcs']
mt_order = [
  'circt-verilator', 'khronos',
  'verilator-1', 'verilator-2', 'verilator-4',
  'repcut-1', 'repcut-2', 'repcut-4', 'repcut-6'
]
palette = sns.color_palette('tab20c')
mt_color = [palette[0], palette[9]] + palette[4:7][::-1] + palette[12:16][::-1]

large_fig_size=(16,2.2)
plat_figure_size=(16,2.0)
bar_width = 1 - 1 / (len(sim_order) + 1)
skip_runs = 3

def filter_simulator(df: pd.DataFrame, sim_order: List[str]):
  df = df.copy()
  df['simulator'] = df['simulator'].replace(rename_simulator)
  sims = df.set_index('simulator').index.unique()
  order = [x for x in sim_order if x in sims]
  return df.set_index('simulator').loc[order].reset_index().copy()

def filter_benchmark(df: pd.DataFrame):
  df = df.copy()
  df['benchmark'] = df['benchmark'].replace(rename_benchmark)
  benchmarks = df.set_index('benchmark').index.unique()
  return df.set_index('benchmark').loc[[x for x in bench_order if x in benchmarks]].reset_index().copy()

def load_perf(file='data/base/result.csv', order: List[str]=None):
  df = pd.read_csv(file)
  df = df[df.run >= skip_runs].copy()
  df = filter_simulator(df, sim_order=order or sim_order)
  df = filter_benchmark(df)
  return df
