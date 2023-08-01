from pathlib import Path

plats = ['base', 'plat-1', 'plat-2']
data_path = Path('data')
bench_order = [
  'SHA256', 'StreamComp',
  'FMUL', 'FPU',
  'Gemmini', 'SIGMA', 'GEMM', 'Conv2D',
  'RISCVMini', 'SodorCore', 'RocketCore',
  'RocketChip'
]
