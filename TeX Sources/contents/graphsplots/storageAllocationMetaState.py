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
# Data for 'Meta-State Block'
MSx = [4,200,200,390,390,580,580,770,770,
	960,960,1150,1150,1300]
MSy = [0,198, 75,265,150,340,183,373,205.5,
	395.5,220.3,410.3,230.2,380.2]
# Plotting
plt.plot(LINx, LINy, '-.k')
plt.plot(RBx, RBy, '--r')
plt.plot(MSx, MSy, 'C2')
# Nameing
plt.xlabel('Transactions (K)')
plt.ylabel('Megabyte')
plt.legend(["BC without optimization",
	"Historic relevant transactions",
	"Meta-State Block"])
# Finalize
plt.grid(b=True, which='major', color='#dddddd',
	linestyle='-.', linewidth=0.4)
plt.tight_layout()
# Output
plt.show()