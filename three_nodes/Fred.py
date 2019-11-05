from cqc.pythonLib import CQCConnection, qubit
import pickle

with CQCConnection("Fred") as Fred:
	q = Fred.recvEPR()
	q1_id = q.get_entInfo().id_AB
	#c1 = pickle.load(Fred.recvClassical())
	c1 = Fred.recvClassical()
	c1 = "".join(chr(x) for x in c1)
	c1_name, c1_id = c1.split(",")
	m = q.measure()
	print("Fred", m)
	print("Fred id", q1_id)
	print("Fred c1 name id", c1_name, c1_id)




