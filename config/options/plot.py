import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np

data = np.genfromtxt("summary.data")
fig, ax = plt.subplots()
labels = [7.1, 7.2, 7.3, 7.4, 8.0, 8.1, 8.2, 8.3, 8.4, 9.0, 9.1, 9.2, 9.3, 9.4, 9.5, 10, 11, 12, 13, 14, 15]
xs = range(len(labels))

def format_fn(tick_val, tick_pos):
    if int(tick_val) in xs:
        return labels[int(tick_val)]
    else:
        return ''


# A FuncFormatter is created automatically.
ax.xaxis.set_major_formatter(format_fn)
ax.xaxis.set_major_locator(MaxNLocator(integer=True))

plt.xticks(np.arange(0, len(labels) + 1, 4))
ax.plot(np.arange(data.shape[0]), data[:, 1])
plt.title("Number of postgresql.conf options per version")
plt.xlabel("PostgreSQL version")
plt.ylabel("Number of options")

plt.savefig("options.png")
