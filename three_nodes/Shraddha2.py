from cqc.pythonLib import CQCConnection, qubit
from lib import *


my_name = "Shraddha"


with CQCConnection("Shraddha") as name_inst:


	qbitdict = node_prepare(name_inst, ["Sothy"], 0)

	print(my_name+"'s qbits:")
	for target in qbitdict:
		print(target, qbitdict[target].measure())

	



