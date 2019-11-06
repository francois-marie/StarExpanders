from cqc.pythonLib import CQCConnection, qubit
rom lib import *
\with CQCConnection('Sothy') as name_inst:
\qbitdict = node_prepare(name_inst, [], 2)
or target in qbitdict:
\print('Sothy', target, qbitdict[target].measure())