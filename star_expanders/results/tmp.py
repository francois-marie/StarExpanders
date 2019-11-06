import json

def protocol_from_json(id, name):
	tree = open_json(id+"_protocol.json")
	return tree[name]

def open_json(name):
    with open(name, encoding='utf-8') as fh:
        data = json.load(fh)
        print(data)
    return (data)


data = protocol_from_json("b", "Sothy")
print(data)