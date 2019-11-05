# StarExpanders

This is the repo code for PEQI hackathon

## TODO

### Create network:

5 nodes w/ names
````Graph(n=5, coupling_map)````

### Connect the nodes indirectly

locally using CZ gates at each node
````node.connect()````

### Erase a qubit

and its connections: Measure Z
````node.erase()````

### Connect neighbors directly

CZ+Y_Y
````DirectConnect(x, y, commun_neighbors)````

### Local complementation

Y measurement
````node.LC()````

### Class

#### Node()

#### Graph()