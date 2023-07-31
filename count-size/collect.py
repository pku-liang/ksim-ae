from pathlib import Path
import re

df = []
for file in Path('./obj').glob('*.txt'):
  data = re.findall(r'\(S\)\s+(\d+) ([^\s]+)', file.read_text())
  result = {
    'name': file.stem
  }
  for val, field in data:
    result[field] = int(val)
  df.append(result)

import pandas as pd
import os
root = Path(os.environ['TEST_ROOT'])
pd.DataFrame(df).to_csv(root.joinpath('results', 'size.csv'), index=False)