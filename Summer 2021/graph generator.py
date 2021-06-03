import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

yrange = range(1988, 2022)

df = pd.read_csv("exoplanet.eu_catalog.csv",
                 usecols = ["planet_status", "discovered", "detection_type"])

conf = df.query("""planet_status    != "unconfirmed"   \
                   & discovered     != "NaN"           \
                   & detection_type != "Controversial" \
                   & detection_type != "Default" """)  \
         .drop(columns = "planet_status")              \
         .replace("Astrometry", "Radial Velocity")     \
         .replace("TTV", "Timing")
         # different names for the same methods

gb = conf.groupby(["discovered", "detection_type"])

methods = sorted(list(set([i[0][1] for i in gb])))

data = {(int(i[0][0]), i[0][1]): int(i[1].size / 2) for i in gb}

df = pd.concat([
    pd.DataFrame(
        [[yr, data.get((yr, mt), 0)]])
    for yr in yrange for mt in methods
], ignore_index = True)

npa = df.to_numpy()
# thanks stackoverflow answer #43094244
npa = np.array(np.split(
                    npa[:, 1],
                    np.cumsum(np.unique(npa[:, 0], return_counts=True)[1])[:-1]
               ))

sums = zip(yrange, [sum(i) for i in npa])
npa = npa.transpose()

mpl.rcParams['text.color'] = 'dimgray'
mpl.rcParams['xtick.color'] = 'dimgray'
mpl.rcParams['ytick.color'] = 'dimgray'

fig = plt.figure(figsize=(15, 10), constrained_layout=True)
ax = fig.add_subplot()

for i in range(len(npa)):
    plt.bar(yrange, npa[i], 0.95, bottom = sum(npa[:i]))
for i in sums:
    ax.annotate(str(i[1]), (i[0], i[1] + 10), va="center", ha="center")

plt.box(False)
ax.grid(axis='y', ls=':')
ax.tick_params(left=False, bottom=False, labelright=True)

plt.xticks(yrange, rotation=45)
plt.yticks(np.arange(0, 1600, 50))

plt.savefig("Confirmed exoplanets by methods EPE.svg")
