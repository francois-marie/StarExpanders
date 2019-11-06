import json

with open("starExpansionTree.json") as f: 
    data= json.load(f)
    '''
    data is dict 
    '''
    finalD ={}
    for p in data:
        finalD[p['place']]=p
    
    print(finalD)
