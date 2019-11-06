from cqc.pythonLib import CQCConnection, qubit
from lib import *


my_name = "Shraddha"


with CQCConnection("Shraddha") as name_inst:


	qbitdict = node_prepare(name_inst, ["Sothy"], 0)
	#print(qbitdict["Sothy"].measure())
	print(my_name+"'s qbits:")
	for target in qbitdict:
		#print(target)
		print(target, qbitdict[target].measure())
		#print(qbitdict[target])

	



