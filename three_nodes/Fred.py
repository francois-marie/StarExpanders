from cqc.pythonLib import CQCConnection, qubit


with CQCConnection("Fred") as Fred:
	q = Fred.recvQubit()
	m = q.measure()
	print(m)



