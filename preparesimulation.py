#Author: D. Kufel
#Date 08/08/2016
'''
Code used to prepare the run of the set of Monte Carlo simulations.
'''
# the Q_10 for AMPARs
Q10_coefficient=2.4
#Temperatures: 25,35,36,37,38,39,40,41,42,43
temperatures= [25.,35.,45.]
tf=[]
for i in range(0,3):
	tf.append(Q10_coefficient**(((temperatures[i]-25.)/10)))
# number of gluatamate molecules in the vesicle list
nlist = [6000, 7000, 8000]

# final fusion pore diameter list
fpD = [0.009,0.008,0.011]

# diffusion coefficient list
diffusion = [3.0e-06, 4.0e-06, 5.0e-06, 6.0e-06]

# position of the vesicle relative to central PSD
vespositions = [0.0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875, 1.0]

counter=0
# Run in parameter space
for T in range(0,1):
	for vespos in range(0,9): #vesicle position (geometry)
		for diffc in range(0,1):	#diffusion constant
			for fpDc in range(0,1):	#final fusion pore diameter (geometry)
				for nc in range (0,1): # number of molecules
					counter+=1
					simidstr = str(counter).rjust(3, '0')
					for run in range(21,41): # number of runs for each parameter set
						runstr= str(run).rjust(3,'0')

						#in main
						filein=open("parameters.mdl",'r')
						fileout=open("run_parameters_"+simidstr+"_"+runstr+".mdl",'w')

						text=filein.read()

						text=text.replace("vesicle_pos = 0.0 ","vesicle_pos= "+str(vespositions[vespos]))
						text=text.replace("tf  = 1.0 ","tf = "+str(tf[int(T)]))
						text=text.replace("n = 6000","n = "+str(nlist[nc]))
						text=text.replace("fpD = 0.001","fpDiameter = "+str(fpD[fpDc]))
						fileout.write(text)

						filein.close()
						fileout.close()

						#in calyx
						filein=open("calyx.mdl",'r')
						fileout=open("calyx_"+simidstr+"_"+runstr+".mdl",'w')

						text = filein.read()
						text=text.replace('parameters.mdl',"run_parameters"+"_"+simidstr+"_"+runstr+".mdl")
						text=text.replace('output.mdl',"output"+"_"+simidstr+"_"+runstr+".mdl")
						fileout.write(text)
						
						#in output
						filein.close()
						fileout.close()

						filein=open("output.mdl",'r')
						fileout=open("output_"+simidstr+"_"+runstr+".mdl",'w')

						text= filein.read()
						text=text.replace("_simid","_"+simidstr+"_"+runstr)
						fileout.write(text)
						
						filein.close()
						fileout.close()




