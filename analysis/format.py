import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
  'font.size': 12,
  'lines.linewidth': 1.5,
  'font.family': 'Arial',
  'font.sans-serif': 'Arial',
  'font.serif': 'Arial',
  'mathtext.fontset': 'custom',
  'mathtext.it': 'Arial:italic',
  'mathtext.rm': 'Arial',
  'axes.titlesize': 14,
  'axes.labelsize': 14,
  'legend.fontsize': 13,
  'legend.title_fontsize': 14,
  'legend.frameon': False,
  'axes.formatter.use_mathtext': True,
  'ytick.labelsize': 12,
  'xtick.labelsize': 12,
  'savefig.transparent': True
})

def mark_npos(bar, ypos, *args, **kws):
  npos = []
  for c in bar.containers:
    for child in c.get_children():
      if np.isnan(child.get_height()):
        center = child.get_x() + child.get_width() / 2
        npos.append(center)
  ylim = plt.ylim()
  xlim = plt.xlim()
  trans = plt.gca().transData
  x0, y0 = trans.transform((xlim[0], ylim[0]))
  _, y1 = trans.transform((xlim[1], ylim[1]))
  inv_trans = trans.inverted()
  _, y = inv_trans.transform((x0, (1 - ypos) * y0 + ypos * y1))
  plt.plot(npos, np.full(len(npos), y), *args, **kws)
  plt.xlim(xlim)

to_latex_format = dict(
  position_float="centering",
  hrules=True,
  position='h!'
)