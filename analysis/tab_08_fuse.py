import pandas as pd
from common import *
from format import *
from scipy.stats import gmean

df = pd.read_csv('data/base/fuse.csv')
df = df.set_index('name').loc[bench_order].reset_index()

df.columns = ['Benchmark', 'Init', 'Opt']
df['Fused'] = 1 - df['Opt'] / df['Init']
fused_mean = 1 - gmean(1 - df['Fused'])
df.loc[len(df)] = ['Average', np.nan, np.nan, fused_mean]

def fmt_pct(s):
  return rf'{s*100:.0f}\%'

s = df.style
s = s.format('{:.0f}', subset=['Init', 'Opt'])
s = s.format(fmt_pct, subset='Fused')
s.hide(axis='index').to_latex(
  'out/tab_08.tex', 
  caption='Init State Size and Fused State Size',
  label='tab:fused',
  **to_latex_format
)