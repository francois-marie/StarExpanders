from cqc.pythonLib import CQCConnection, qubit
from lib import *


my_name = "Shraddha"
targets = ["Sothy"]
n_receive = 0

with CQCConnection(my_name) as name_inst:


	qbitdict = node_prepare(name_inst, targets, n_receive)
	#print(qbitdict["Sothy"].measure())
	#print(my_name+"'s qbits:")
	for target in qbitdict:
		#print(target)
		print(my_name, target, qbitdict[target].measure())
		#print(qbitdict[target])

	



