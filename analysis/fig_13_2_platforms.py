from fig_10_2_single_thread import *

sim_order.remove('vcs')
plot(load_perf(f'data/{plats[2]}/result.csv'), False)
plt.savefig('out/fig_13_2.pdf')