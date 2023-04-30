import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("pgbench_log.17801", encoding='utf-8')
sns.displot(data=data[:, 2])

plt.xlim([0, 1000])
plt.savefig("latency-hist.png")
