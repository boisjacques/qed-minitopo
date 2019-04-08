import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

titles = ["nlnd", "nlmd", "nlhd", "mlnd", "mlmd", "mlhd", "hlnd", "hlmd", "hlhd"]
plotData = pd.DataFrame(np.random.rand(20, 9), columns=titles)
failureRates = pd.DataFrame(np.random.rand(9, 1), index=titles)
color = {'boxes': 'DarkGreen', 'whiskers': 'DarkOrange', 'medians': 'DarkBlue', 'caps': 'Gray'}
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax2 = ax1.twinx()
plotData.plot.box(ax=ax1, color=color, sym='+')
failureRates.plot(ax=ax2, color='b', legend=False)
ax1.set_ylabel('Seconds')
ax2.set_ylabel('Failure Rate in %')
plt.xlim(-0.7, 8.7)
ax1.set_xticks(range(len(titles)))
ax1.set_xticklabels(titles)
fig.tight_layout()
fig.show()
print ""