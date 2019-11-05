from cqc.pythonLib import CQCConnection, qubit


def receive_link(name_inst, n_receive):
	qbitdict = {}
	rqbits = []
	senders = {} 
	for i in range(n_receive):
		rqbits.append(name_inst.recvEPR())
		message = name_inst.recvClassical()
		c1 = "".join(chr(x) for x in message)
		c1_name, c1_id = c1.split(",")
		senders[int(c1_id)] = c1_name
		#print(senders)

	for q in rqbits:
		q_id = q.get_entInfo().id_AB
		#print("q_id", q_id)
		qbitdict[senders[q_id]] = q

	return qbitdict


def send_link(name_inst, target):
	q = name_inst.createEPR(target)
	q_id = q.get_entInfo().id_AB
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




	
