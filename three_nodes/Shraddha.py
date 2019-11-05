from cqc.pythonLib import CQCConnection, qubit


with CQCConnection("Shraddha") as Shraddha:
	nqubits = 4
	qubits = []
	for i in range(nqubits):
		q = qubit(Shraddha)
		q.H()
		qubits.append(q)
    

	qubits[0].cphase(qubits[1])
	qubits[2].cphase(qubits[3])


	Shraddha.sendQubit(qubits[0], "Sothy")
	Shraddha.sendQubit(qubits[2], "Fred")
	m1 = qubits[1].measure()
	m2 = qubits[3].measure()
	print(m1)
	print(m2)
	Shraddha.flush()



