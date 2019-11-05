from cqc.pythonLib import CQCConnection, qubit
from lib import *
with CQCConnection('FM') as name_inst:
	qbitdict = node_prepare(name_inst, [], 1)
	for target in qbitdict:
		print('FM', target, qbitdict[target].measure())