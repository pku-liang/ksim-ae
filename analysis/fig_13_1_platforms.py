from fig_10_2_single_thread import *

plot(load_perf(f'data/{plats[1]}/result.csv'), False)
plt.savefig('out/fig_13_1.pdf')