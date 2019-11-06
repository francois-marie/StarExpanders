# StarExpanders

![alt text](https://github.com/francois-marie/StarExpanders/blob/master/distribute_GHZ_arbitrary_network.png)

images by Clément Meignant

This repository has be made during the 2019 edition of the Pan-European Quantum Internet Hackathon — Paris Node, on November 5th and 6th, 2019.

It deals with Distributing Graph States Over Arbitrary Quantum Networks using Simulaqron.

The paper can be found at the following URL:
https://arxiv.org/pdf/1811.05445.pdf

This project uses Simulaqron, an application level simulator for a quantum internet:
http://www.simulaqron.org/

## Commands to run the repository

````
git clone https://github.com/francois-marie/StarExpanders


````


## Creation of the graph

````network.py````
generates a json file descriptive of the directional network with specific id and a specific folder for the protocol execution
````id_network.json````
Creates the protocol for the execution of the nodes to go from the network to a GHZ of specified nodes
````id_protocol.json````
TODO: generate protocol automatically from the network and the list of target nodes

## Generate simulacron

````network2local.py````
Generated two bash scripts
* To start the simulacron network
````start.sh````
* To execute the protocol on the nodes
````run.sh````

## Run the protocol

````start.sh````

````run.sh```` calls ````run_node.py```` to generate the CQCConnection for each node and execute the protocol for star expansions.

## DONE

### Create network:
````
{"alpha": {
    "my_name": "alpha",
    "target": [beta],
    "receivers": 2
    },
    ...
    }
````

### Connect the nodes indirectly

locally using CZ gates at each node

### Erase a qubit

and its connections: Measure Z

### Connect neighbors directly

CZ+Y_Y

## TODO

### Local corrections

Implement local corrections for GHZ star expansion

### Protocol Generation

Generate automatically the protocol to get GHZ from a graph given a list of targets


![alt text](https://github.com/francois-marie/StarExpanders/blob/master/Steiner_tree.png)
![alt text](https://github.com/francois-marie/StarExpanders/blob/master/generalized_entanglement_swapping.png)