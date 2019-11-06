from cqc.pythonLib import CQCConnection, qubit
from lib import *
with CQCConnection('Fred') as name_inst:
	qbitdict = node_prepare(name_inst, ['Georg'], 0)
	for target in qbitdict:
		print('Fred', target, qbitdict[target].measure())