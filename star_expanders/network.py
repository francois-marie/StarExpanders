'''
node = "Sothy"
targets = []
n_receive = 2


node = "Shraddha"
targets = ["Sothy"]
n_receive = 0

node = "Fred"
targets = ["Georg"]
n_receive = 0

node= "Georg"
targets = ["Sothy", "FM"]
n_receive = 1

node="FM"
targets=[]
n_receive=1
'''
import json


graph = {'Sothy': [],
           'Shraddha': ['Sothy'],
             'Fred': ['Georg'],
             'Georg': ['Sothy',"FM"],
             'FM': [],}

def calculate_n_receive(graph):
    outdic={name:0 for name in graph}
    for name in graph:
        for target in graph[name]:
            outdic[target]+=1
    return outdic

'''
print( calculate_n_receive(graph))
'''

def print_nodes_conf(graph):
    n_receive=calculate_n_receive(graph)
    '''
    for name in graph:
        print("\n")
        print('node="'+name+'"')
        print('targets=',graph[name])
        print('n_receive=', n_receive[name])
    '''
    node=json.dumps([{'node': name, 'targets': graph[name], 'n_receive': n_receive[name]} for name in graph], indent=4)
    with open('nodes.json','w') as f:
        print(node, file=f)
def main():
    print_nodes_conf(graph)

if __name__=="__main__":
    main()
