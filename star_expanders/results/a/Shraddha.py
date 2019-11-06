from cqc.pythonLib import CQCConnection, qubit
from lib import *
with CQCConnection('Shraddha') as name_inst:
	qbitdict = node_prepare(name_inst, ['Sothy', 'FM'], 0)
	for target in qbitdict:
		print('Shraddha', target, qbitdict[target].measure())