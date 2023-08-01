import pandas as pd
import json
from common import *
import re

cpuinfo = []

def clean_value(s):
  s = re.sub(r'\(\d instances?\)', '', s)
  s = re.sub(r'\d-Core Processor', '', s)
  s = re.sub(r'with.*', '', s)
  s = re.sub(r'Intel\(R\) Core\(TM\)|AMD', '', s)
  s = re.sub(r'Ryzen \d', r'Ryzen', s)
  s = re.sub(r'CPU @ [0-9.]+GHz', '', s)
  s = re.sub(r'(\d\d\d\d).\d\d\d\d', r'\1 MHz', s)
  return s.strip()

for plat in plats:
  cpu_info = json.loads(data_path.joinpath(plat, 'cpu-info.json').read_text())
  index = [x['field'].strip().rstrip(':') for x in cpu_info['lscpu']]
  value = [x['data'].strip() for x in cpu_info['lscpu']]
  ser = pd.Series(value, index=index)
  ser = ser[['Model name', 'CPU max MHz', 'L1d cache', 'L1i cache', 'L2 cache', 'L3 cache']]
  ser.index = ['CPU', 'Max Frequency', 'L1i', 'L1d', 'L2', 'L3']
  ser = ser.apply(clean_value)
  cpuinfo.append(ser)

pd.DataFrame(cpuinfo, index=plats).T.style.hide(axis='index').to_latex(
  'out/tab_07_1.tex',
  caption='Evaluation Settings 1',
  position_float="centering",
  hrules=True
)
