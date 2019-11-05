from cqc.pythonLib import CQCConnection, qubit


with CQCConnection("Sothy") as Sothy:
	q = Sothy.recvEPR()
	m = q.measure()
	print("Sothy", m)



