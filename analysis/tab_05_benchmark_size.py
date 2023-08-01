import pandas as pd
from common import *
from format import *

fields = ["name","num-ops","num-edges"]
name = ["Benchmark","IR Nodes","IR Edges"]
df = pd.read_csv(f'data/{plats[0]}/size.csv')
df = df[fields]
df.columns = name

s = df.set_index('Benchmark').loc[bench_order].reset_index().style
s.set_table_styles([{'selector': '', 'props': ':small'}])
s.hide(axis='index').to_latex(
  'out/tab_05.tex',
  caption='Benchmark used in Khronos',
  label='tab:bench-size',
  **to_latex_format
)