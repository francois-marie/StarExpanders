from cqc.pythonLib import CQCConnection, qubit
from lib import *
with CQCConnection('Sothy') as name_inst:
	qbitdict = node_prepare(name_inst, [], 2)
	for target in qbitdict:
		print('Sothy', target, qbitdict[target].measure())