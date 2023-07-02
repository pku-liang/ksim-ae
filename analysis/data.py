import numpy as np
import pandas as pd

order = [
  'SHA256',
  'StreamComp',
  'FMUL',
  'FPU',
  'Gemmini',
  'SIGMA',
  'GEMM',
  'Conv2D',
  'RISCVMini',
  'SodorCore',
  'RocketCore',
]

rename_simulator = {
  'ksim': 'khronos',
}
baseline_name = 'circt-verilator'
ours = 'khronos'

sim_order = ['circt-verilator', 'verilator-1', 'verilator-2', 'verilator-4', 'khronos', 'essent', 'repcut-1', 'repcut-2', 'repcut-4', 'vcs']

large_fig_size=(16,3)

skip_runs = 3

def filter_simulator(df: pd.DataFrame):
  df = df.copy()
  df['simulator'] = df['simulator'].replace(rename_simulator)
  return df.set_index('simulator').loc[sim_order].reset_index().copy()

def filter_benchmark(df: pd.DataFrame):
  return df.set_index('benchmark').loc[order].reset_index().copy()

def load_perf(file='../results/result.csv'):
  df = pd.read_csv(file)
  df = df[df.run >= skip_runs].copy()
  df = filter_simulator(df)
  df = filter_benchmark(df)
  return df