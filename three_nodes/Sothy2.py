from cqc.pythonLib import CQCConnection, qubit
from lib import *


my_name = "Sothy"

with CQCConnection("Sothy") as name_inst:

	qbitdict = node_prepare(name_inst, [], 1)

	print(my_name+"'s qbits:")
	for target in qbitdict:
		print(target, qbitdict[target].measure())

	