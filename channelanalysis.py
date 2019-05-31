#Author D.Kufel
#Date: 09/08/2016
'''
File to analyze the data from the Monte Carlo simulation - calculating the average fraction of channels in any state. Used to find the fraction of unbound channels (Figure 4).
'''
statelist=["C0","C1","C2","C3","C4","O1","O2","O3","O4","D1","D2","D3","D4"]
for state in statelist:
	file=open("Average_AMPA_"+state+"_25.dat",'w')

	import csv

	listaverages=[]

	csv_reader0=csv.reader(open("AMPAR_"+state+"_001_001.dat"),delimiter=" ")
	for row in csv_reader0:
		listaverages.append(float(row[1]))

	for vesicle in range(1,10):
		for run_number in range(1,41):
			if vesicle!=1 and run_number!=1:
				nStrv=str(vesicle).rjust(3, '0')  
				nStrr=str(run_number).rjust(3, '0') 
				name="AMPAR_"+state+"_"+nStrv+"_"+nStrr+".dat"
				print(name)
				csv_reader=csv.reader(open(name), delimiter=" ")
				counter=0
				for row in csv_reader:
					listaverages[counter]+=float(row[1])
					counter+=1

	i=0
	for k in listaverages:
		file.write(str(i))
		file.write(" ")
		file.write(str(k/360.))
		file.write("\n")
		i+=1
