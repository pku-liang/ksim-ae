import pandas as pd
from common import *

pd.read_csv(f'data/{plats[0]}/extra-info.csv').style.hide(axis='index').to_latex(
  'out/tab_07_2.tex',
  caption='Evaluation Settings 2'
)