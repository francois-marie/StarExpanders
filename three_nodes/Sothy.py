from cqc.pythonLib import CQCConnection, qubit


with CQCConnection("Sothy") as Sothy:
	q = Sothy.recvQubit()
	m = q.measure()
	print(m)



