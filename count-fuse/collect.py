from pathlib import Path
import re

df = []
for file in Path('./obj').glob('*.txt'):
  data = file.read_text()
  init_cost = int(re.search(r'It: 0 Cost: (\d+)', data).group(1))
  final_cost = int(re.search(r'FinalCost: (\d+)', data).group(1))
  result = {
    'name': file.stem,
    'init': init_cost,
    'opt': final_cost
  }
  df.append(result)

import pandas as pd
import os
root = Path(os.environ['TEST_ROOT'])
pd.DataFrame(df).to_csv(root.joinpath('results', 'fuse.csv'), index=False)