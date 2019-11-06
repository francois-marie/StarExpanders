from cqc.pythonLib import CQCConnection, qubit
rom lib import *
\with CQCConnection('Fred') as name_inst:
\qbitdict = node_prepare(name_inst, ['Georg'], 0)
or target in qbitdict:
\print('Fred', target, qbitdict[target].measure())