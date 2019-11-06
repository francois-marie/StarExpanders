from cqc.pythonLib import CQCConnection, qubit
import json

def receive_link(name_inst, n_receive):
	qbitdict = {}
	rqbits = []
	senders = {}
	for i in range(n_receive):
		rqbits.append(name_inst.recvEPR())
		message = name_inst.recvClassical()
		c1 = "".join(chr(x) for x in message)
		#print('message', name_inst.name, message)
		c1_name, c1_id = c1.split(",")
		senders[int(c1_id)] = c1_name
		#print(senders)
	#print(name_inst.name, rqbits)
	for q in rqbits:
		#print(name_inst.name, [q])
		q_id = q.get_entInfo().port_B
		#print(name_inst.name, "port_B", q.get_entInfo().port_B)

		qbitdict[senders[q_id]] = q
		#print(name_inst.name, senders)

	return qbitdict


def send_link(name_inst, target):
	q = name_inst.createEPR(target)
	#print(name_inst.name, "sending port_A", q.get_entInfo().id_AB, q.get_entInfo().port_A)
	q_id = q.get_entInfo().port_A
	message = name_inst.name+", "+str(q_id)
	name_inst.sendClassical(target, [ord(c) for c in message])
	return q

def node_prepare(name_inst, targets, n_receive):
	#with CQCConnection(name) as name_inst:
	qbitdict = receive_link(name_inst, n_receive)

	for target in targets:
		qbitdict[target] = send_link(name_inst, target)
		#print(qbitdict[target].measure())
	return qbitdict

def params_from_json(id, name):
	"""
	returns list of strings and int

	Arguments:
		id {str} -- id of the network
		name {str} -- name of the node
	"""
	#network = open_json("results/"+id+"_network.json")
	network = open_json("../"+id+"_network.json")
	node = network[name]
	return(node["target"], node["receivers"])

def protocol_from_json(name):
	tree = open_json("starExpansionTree.json")
	return tree[name]

def open_json(name):
    with open(name, encoding='utf-8') as fh:
        data = json.load(fh)
    return (data)


def star_expansion(my_qubit_dict, name_inst, source, targets):
	"""does the star expansion of the target from the source

	Arguments:
		my_qubit_dict {dict{simulacronQubitObject}} -- [description]
		name_inst {SimulacronCQCConnectionObjct} -- [description]
		source {str} -- [description]
		targets {str} -- [description]

	Returns:
		[type] -- [description]
	"""
	my_name = name_inst.name
	protocol = protocol_from_json(my_name)
	if targets==[my_name]: # (aka do nothing)
		return my_qubit_dict
	else:
		if my_name in targets:
			my_qubit_dict[my_name] = (name_inst.qubit()).H()
		q_aux = name_inst.qubit()
		q_aux.H()
		q_aux.cphase(my_qubit_dict[source])
		for target in targets:
			q_aux.cphase(my_qubit_dict[target])
		q_aux.Y()
		m1 = q_aux.measure()
		for t in targets:
			if t != my_name:
				m2 = (my_qubit_dict[t].Y()).measure()
		return my_qubit_dict