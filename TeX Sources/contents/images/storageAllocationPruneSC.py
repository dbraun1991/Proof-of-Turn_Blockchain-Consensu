# Imports
from matplotlib import pyplot as plt
# Dimensions
plt.figure(figsize=(21*0.36,9*0.36))
# Data for 'Linear'
LINx = [0,1300]
LINy = [0,1300]
# Data for 'Relevant Blocks'
RBx = [50,650,1300]
RBy = [0,300,625]
# Data for 'Prune Procedure/Sidechains'
SCx = [4,150,150,300,300,450,450,600,600,750,750,900,900,1050,1050,1200,1200,1300]
SCy = [0,146,75,225,150,300,225,375,300,450,375,525,450,600,525,675,600,700]
# Plotting
plt.plot(LINx, LINy, 'k')
plt.plot(RBx, RBy, 'r')
plt.plot(SCx, SCy, 'C0')
# Nameing
plt.xlabel('Transactions (K)')
plt.ylabel('Megabyte')
plt.legend(["BC without optimization", "Historic relevant transactions", "Prune Procedure/Child-chains", ])
# Finalize
plt.grid(b=True, which='major', color='#dddddd', linestyle='-.', linewidth=0.4)
plt.tight_layout()
# Output
plt.show()
