from cqc.pythonLib import CQCConnection, qubit
from lib import *
with CQCConnection('Georg') as name_inst:
	qbitdict = node_prepare(name_inst, ['Sothy', 'FM'], 1)
	for target in qbitdict:
		print('Georg', target, qbitdict[target].measure())