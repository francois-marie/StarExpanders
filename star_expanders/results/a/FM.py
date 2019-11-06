from cqc.pythonLib import CQCConnection, qubit
rom lib import *
\with CQCConnection('FM') as name_inst:
\qbitdict = node_prepare(name_inst, [], 1)
or target in qbitdict:
\print('FM', target, qbitdict[target].measure())