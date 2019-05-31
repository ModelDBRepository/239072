#Author: D.Kufel
#Date: 05/01/2018

'''
The following code calculates the skewness and variation of the AMPAR conductances
distribution (for different runs of simulations).
Used in the data analysis of the Monte Carlo simulation.
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import variation,skew

statelist=["O1","O2","O3","O4"]

listnewO1=[]
listnewO2=[]
listnewO3=[]
listnewO4=[]

for state in statelist:
	
	for vesicle in range(1,10):
		for run_number in range(1,41):
			nStrv=str(vesicle).rjust(3, '0')  
			nStrr=str(run_number).rjust(3, '0') 
			name="AMPAR_"+state+"_"+nStrv+"_"+nStrr+".dat"
			x,y=np.loadtxt(open(name), delimiter=" ", unpack=True)
			print(name, np.max(y))
			if state=="O1":
				listnewO1.append(np.max(y))
			elif state=="O2":
				listnewO2.append(np.max(y))
			elif state=="O3":
				listnewO3.append(np.max(y))
			else:
				listnewO4.append(np.max(y))



arrayO1=np.asarray(listnewO1)
arrayO2=np.asarray(listnewO2)
arrayO3=np.asarray(listnewO3)
arrayO4=np.asarray(listnewO4)


merged=arrayO1*0.1+arrayO2*0.4+arrayO3*0.7+arrayO4
print(merged)
print("CV=",round(variation(merged),2),"Skewness=",round(skew(merged),2))

plt.figure()

plt.hist(merged,bins=25, normed=1,facecolor='black',histtype='bar', ec='white')

plt.xlabel('amplitude (open channels scaled)')
plt.ylabel('Number (norm.)')
plt.show()
