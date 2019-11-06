import json

with open("starExpansionTree.json") as f: 
    data= json.load(f)
    '''
    data is dict 
    '''
    finalD ={}
    for p in data:
        finalD[p["place"]]=p
    
    print(finalD)
    with open("star_expanders/results/b_protocol.json", 'w') as f:
        print(finalD, file=f)