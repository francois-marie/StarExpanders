#from cqc.pythonLib import CQCConnection, qubit
#from lib import *
import json

def generate_python_file_from_node(folder_prefix, my_name, targets, n_receive):
	with open(folder_prefix+my_name+".py", 'w')  as f:
			f.write("from cqc.pythonLib import CQCConnection, qubit\n\
	from lib import *\n\
	with CQCConnection('"+my_name+"') as name_inst:\n\
		qbitdict = node_prepare(name_inst, "+str(targets)+", "+str(n_receive)+")\n\
		for target in qbitdict:\n\
			print('"+my_name+"', target, qbitdict[target].measure())")
	return

def generate_files_from_network(id):
	"""routine that generates the python files for a network given with its id

	Arguments:
		id {[type]} -- [description]
	"""
	folder_prefix = "results/"+id+"/"
	network_prefix = "results/"+id
	g = open(network_prefix+'network.json', 'r')
	data = json.load(g)
	names = []
	for node in data:
		my_name = data[node]['my_name']
		names.append(my_name)
		targets = data[node]['target']
		n_receive = data[node]['receivers']

		generate_python_file_from_node(folder_prefix,  my_name, targets, n_receive)

	g.close()



	with open(folder_prefix+'run.sh', 'w')  as f:
		for name in names:
			if name!=names[-1]:
				f.write('python '+name+'.py &\n')
			else:
				f.write('python '+name+'.py\n')


	with open(folder_prefix+'start.sh', 'w')  as f:
		f.write('simulaqron reset\nsimulaqron set backend qutip\nsimulaqron start --nodes ')
		for name in names:
			if name!=names[-1]:
				f.write(name+',')
			else:
				f.write(name)
	return

if __name__ == "__main__":
	generate_files_from_network("a")