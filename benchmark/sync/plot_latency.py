import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

import sys

data = np.genfromtxt("pgbench_log.11769", encoding='utf-8')
sync_data = np.genfromtxt("synclat.data", encoding='utf-8')

plt.plot(data[:, 2])
plt.plot(sync_data / 1000)
plt.savefig("sync.png")
