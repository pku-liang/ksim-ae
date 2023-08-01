import pandas as pd
from common import *
from format import *

s = pd.read_csv(f'data/{plats[0]}/extra-info.csv').style
s.set_table_styles([{'selector': '', 'props': ':small'}])
s.hide(axis='index').to_latex(
  'out/tab_07_2.tex',
  caption='Evaluation Settings 2',
  label='tab:setup-2',
  **to_latex_format
)