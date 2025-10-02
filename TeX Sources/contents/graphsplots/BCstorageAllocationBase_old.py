# Imports
from matplotlib import pyplot as plt
# Data for 'Linear'
plt.figure(figsize=(21*0.36,9*0.36))
# Data for 'Linear'
LINx = [0,1300]
LINy = [0,1300]
# Data for 'Relevant Transactions'
RBx = [50,650,1300]
RBy = [0,300,625]
# Plotting
plt.plot(LINx, LINy, 'k')
plt.plot(RBx, RBy, 'r')
# Nameing
plt.xlabel('Blocks')
plt.ylabel('Megabyte')
plt.legend(["BC without optimization",
	"Historic relevant Blocks"])
# Finalize
plt.grid(b=True, which='major', color='#dddddd',
	linestyle='-.', linewidth=0.4)
plt.tight_layout()
# Output
plt.show()