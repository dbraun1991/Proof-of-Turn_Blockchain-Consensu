# Imports
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np
# Output dimensions
plt.figure(figsize=(21*0.36,9*0.36))

# Case 1: n nodes and groups of 1 .. Y = 1
def f1(n):
    return n/n
# Case 2: n nodes and Groups of two nodes
def f2(n):
    return (n/2)/n
# Case 3: n nodes and Groups of three nodes
def f3(n):
    return (n/3)/n

# Case 5: n nodes and three groups
def f5(n):
    return 3/n
# Case 6: n nodes and four groups
def f6(n):
    return 4/n
# Case 7: n nodes and four groups
def f7(n):
    return 5/n
# Plot Ranges
rnge1 = np.arange(2.9, 54.01, 0.1)
rnge3 = np.arange(3, 55, 1)
rnge4 = np.arange(4, 55, 1)
rnge5 = np.arange(5, 55, 1)
rnge6 = np.arange(6, 55, 1)
rnge9 = np.arange(9, 55, 1)

# Plots
plt.plot(rnge3, f5(rnge3), '--', linewidth=2, label="\u03B1: Three groups")
plt.plot(rnge4, f6(rnge4), '--', linewidth=2, label="\u03B2: Four groups")
plt.plot(rnge5, f7(rnge5), '--', linewidth=2, label="\u03B3: Five groups")

plt.plot(rnge1, f1(rnge1), 'tab:red', linewidth=2, label="\u03B4: Full mistrust")
plt.plot(rnge6, f2(rnge6), 'tab:brown',  linewidth=2, label="\u03B5: Groups of (~)two nodes")
plt.plot(rnge9, f3(rnge9), 'tab:olive', linewidth=2, label="\u03B8: Groups of (~)three nodes")
# Axis & Labels
plt.xlabel('Network nodes')
plt.ylabel('Hostile nodes')
def to_percent(y, position):
    s = str(round(100*y,1))
    return s + '%'
formatter = FuncFormatter(to_percent)
plt.gca().yaxis.set_major_formatter(formatter)
# Finalize
plt.grid(b=True, which='major', color='#aaaaaa',
	linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#aaaaaa',
	linestyle='-.', alpha=0.2)
plt.legend(bbox_to_anchor=(0.575, 0.9), loc='upper left')
plt.tight_layout()
# Output
plt.show()
