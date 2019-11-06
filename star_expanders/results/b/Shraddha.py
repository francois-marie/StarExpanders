from cqc.pythonLib import CQCConnection, qubit
rom lib import *
\with CQCConnection('Shraddha') as name_inst:
\qbitdict = node_prepare(name_inst, ['Sothy'], 0)
or target in qbitdict:
\print('Shraddha', target, qbitdict[target].measure())