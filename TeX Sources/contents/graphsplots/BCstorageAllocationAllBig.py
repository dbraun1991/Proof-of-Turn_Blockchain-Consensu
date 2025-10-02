# Imports
from matplotlib import pyplot as plt
# Dimensions
plt.figure(figsize=(21*0.36,9*0.36))
# Data for 'Linear'
LINx = [0,2050]
LINy = [0,2050]
# Data for 'Relevant Blocks'
RBx = [50,650,1300,2050]
RBy = [0,300,625,1000]
# Data for 'Prune Procedure/Sidechains'
SCx = [4,150,150,300,300,450,450,600,600,750,750,
	900,900,1050,1050,1200,1200,1350,1350,1500,1500,
	1650,1650,1800,1800,1950,1950,2050]
SCy = [0,146, 75,225,150,300,225,375,300,450,375,
	525,450,600,525,675,600,750,675,825,750,900,
	825,975,900,1050,975,1075]
# Data for 'Meta-State Block'
MSx = [4,200,200,390,390,580,580,770,770,960,960,1150,
1150,1340,1340,1530,1530,1720,1720,1910,1910,2000,2050]
MSy = [0,198, 75,265,150,340,183.3,373,205,395,220,410,
230,420.2,236,426.8,241.2,431,244.1,434,246.1,336,386.1]
# Plotting
plt.plot(LINx, LINy, '-.k')
plt.plot(RBx, RBy, '--r')
plt.plot(SCx, SCy, 'C0')
plt.plot(MSx, MSy, 'C2')
# Nameing
plt.xlabel('Transactions (K)')
plt.ylabel('Megabyte')
plt.legend(["BC without optimization",
	"Historic relevant transactions",
	"Prune Procedure/Child-chains",
	"Meta-State Block"])
# Finalize
plt.grid(b=True, which='major', color='#dddddd',
	linestyle='-.', linewidth=0.4)
plt.tight_layout()
# Output
plt.show()