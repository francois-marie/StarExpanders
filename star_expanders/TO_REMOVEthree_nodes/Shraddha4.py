from cqc.pythonLib import CQCConnection, qubit
from lib import *
import json

f = open('Shraddha4.json', 'r')
data = json.load(f)
my_name = data['my_name']
targets = data['target']
n_receive = data['receivers']

with CQCConnection(my_name) as name_inst:


	qbitdict = node_prepare(name_inst, targets, n_receive)
	#print(qbitdict["Sothy"].measure())
	#print(my_name+"'s qbits:")
	for target in qbitdict:
		#print(target)
		print(my_name, target, qbitdict[target].measure())
		#print(qbitdict[target])

	



