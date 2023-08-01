from tab_09_ipc import *

make_table(load_perf(), 'OPS').to_latex(
  'out/tab_10.tex',
  caption='Instructions Per Cycle',
  position_float="centering",
  hrules=True
)