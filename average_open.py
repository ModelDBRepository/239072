#Author: Dominik Kufel
#Date: 05/01/2018
'''
The following code will give a total conductance of the AMPA type receptor.
Used in data analysis of the Monte Carlo simulation.
'''

import numpy as np
import matplotlib.pyplot as plt


name1="Average_AMPA_O1_25.dat"
name2="Average_AMPA_O2_25.dat"
name3="Average_AMPA_O3_25.dat"
name4="Average_AMPA_O4_25.dat"

x,y1=np.loadtxt(open(name1), delimiter=" ", unpack=True)
x,y2=np.loadtxt(open(name2), delimiter=" ", unpack=True)
x,y3=np.loadtxt(open(name3), delimiter=" ", unpack=True)
x,y4=np.loadtxt(open(name4), delimiter=" ", unpack=True)

merged=0.1*y1+0.4*y2+0.7*y3+1.0*y4

plt.plot(x,merged)
plt.show()
