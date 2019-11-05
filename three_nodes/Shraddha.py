from cqc.pythonLib import CQCConnection, qubit
import pickle

def s2i(message):
	return [ord(c) for c in message]

with CQCConnection("Shraddha") as Shraddha:

	q1 = Shraddha.createEPR("Sothy")
	q1_id = q1.get_entInfo().id_AB
	#Shraddha.sendClassical("Sothy", "Shraddha, "+str(q1_id))
	
	q2 = Shraddha.createEPR("Fred")
	q2_id = q2.get_entInfo().id_AB
	message = "Shraddha, "+str(q2_id)
	#Shraddha.sendClassical("Fred", pickle.dumps(message))
	Shraddha.sendClassical("Fred", s2i(message))
	print(Shraddha.name)
	

	m1 = q1.measure()

	m2 = q2.measure()
	print("Shradda to Sothy", m1)
	print("Shradda to Fred", m2)
	print("Shradda to Sothy id", q1_id)
	print("Shradda to Fred id", q2_id)
	



