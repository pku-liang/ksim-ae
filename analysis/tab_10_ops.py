from tab_09_ipc import *

make_table(load_perf(), 'OPS', highlight='min').to_latex(
  'out/tab_10.tex',
  caption='Instruction Counts (G)',
  label='tab:ops',
  **to_latex_format
)