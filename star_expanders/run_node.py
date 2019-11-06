from cqc.pythonLib import CQCConnection, qubit
from lib import *
import json
import sys

my_name = sys.argv[1]
network_id = sys.argv[2]

targets, n_receive = params_from_json(network_id, my_name)

#f = open('Shraddha4.json', 'r')
#data = json.load(f)
#my_name = data['my_name']
#targets = data['target']
#n_receive = data['receivers']



with CQCConnection(my_name) as name_inst:


	qbitdict = node_prepare(name_inst, targets, n_receive)
	for target in qbitdict:
		print(my_name, target, qbitdict[target].measure())


	





















#from cqc.pythonLib import CQCConnection, qubit
#from lib import *
import json

g = open('network.json', 'r')
data = json.load(g)
names = []
for node in data:
	my_name = data[node]['my_name']
	names.append(my_name)
	targets = data[node]['target']
	n_receive = data[node]['receivers']

	with open(my_name+".py", 'w')  as f:
		f.write("from cqc.pythonLib import CQCConnection, qubit\n\
from lib import *\n\
with CQCConnection('"+my_name+"') as name_inst:\n\
	qbitdict = node_prepare(name_inst, "+str(targets)+", "+str(n_receive)+")\n\
	for target in qbitdict:\n\
		print('"+my_name+"', target, qbitdict[target].measure())")

g.close()



with open('run.sh', 'w')  as f:
	for name in names:
		if name!=names[-1]:
			f.write('python '+name+'.py &\n')
		else:
			f.write('python '+name+'.py\n')


with open('start.sh', 'w')  as f:
	f.write('simulaqron reset\nsimulaqron set backend qutip\nsimulaqron start --nodes ')
	for name in names:
		if name!=names[-1]:
			f.write(name+',')
		else:
			f.write(name)
