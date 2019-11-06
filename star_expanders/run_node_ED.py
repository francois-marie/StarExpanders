from cqc.pythonLib import CQCConnection, qubit
from lib import *
import json
import sys, time

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
	#print(name_inst.name, "node prepare complete")
	#time.sleep(1)
	#protocol = protocol_from_json(network_id, name_inst.name)
	#source = protocol['source']
	#targets = protocol['targets']
	#qbitdict = star_expansion(qbitdict, name_inst, source, targets)
	for target in qbitdict:
		print(my_name, target, qbitdict[target].measure())




	

















