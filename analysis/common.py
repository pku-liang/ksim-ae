from pathlib import Path

plats = ['base', 'plat-2', 'plat-3']
data_path = Path('data')
bench_order = [
  'SHA256', 'StreamComp',
  'FMUL', 'FPU',
  'Gemmini', 'SIGMA', 'GEMM', 'Conv2D',
  'RISCVMini', 'SodorCore', 'RocketCore',
  'RocketChip'
]
