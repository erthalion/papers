import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

data = np.genfromtxt("pgbench_log.17801", encoding='utf-8')
kde = gaussian_kde(data[:, 2])
dist_space = np.linspace(0, 1000, 1000)

plt.plot(dist_space, kde(dist_space))
plt.savefig("latency-kde.png")
