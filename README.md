# StarExpanders

## [Entanglement Routing]

![alt text](https://github.com/francois-marie/StarExpanders/blob/master/distribute_GHZ_arbitrary_network.png)

images by Clément Meignant

This repository has be made during the 2019 edition of the Pan-European Quantum Internet Hackathon — Paris Node, on November 5th and 6th, 2019.

It deals with Distributing Graph States Over Arbitrary Quantum Networks using Simulaqron.

The paper can be found at the following URL:
https://arxiv.org/pdf/1811.05445.pdf

This project uses Simulaqron, an application level simulator for a quantum internet:
http://www.simulaqron.org/

## Bash script

The package needs Simulaqron to work properly
PYTHONPATH should be in the Simulaqron directory

````
git clone https://github.com/francois-marie/StarExpanders
cd StarExpanders
export PYTHONPATH=$(pwd):$PYTHONPATH
python network.py
python network2local.py
./start.sh
./run.sh

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
{"alpha": {                 # Node number 1
    "my_name": "alpha",     # Node name
    "target": ["beta"],     # Node number 1 sends one qubit of EPR pair to Nodes in "target" list
    "receivers": 2          # Node number 1 receives one qubit of EPR pair sent by 2 receivers. (port_A) identifies the sender
    },
    ...
    }
````

### GHZ state

Create GHZ state
````
[
    {
        "place": "gamma",       # Node at which GHZ state preparation takes place. Node isolated in the final GHZ state
        "source": "delta",      # Center node in the final GHZ state
        "targets": ["gamma"]    # Nodes connected in the GHZ state to the center node
    },
    ...
]
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

## Authors

This example was created at the Pan-European Quantum Internet Hackathon — Paris Node, on November 5th and 6th, 2019.

The team members were:
* Frederic Grosshans
* Shraddha Singh
* Georg Harder
* Sivasothy Shanmugalingam
* Francois-Marie Le Régent

You can play a demo of the final run of the protocol using the following command:

````
sudo apt-get install ttyrec
sudo apt-get install imagemagick
sudo apt-get install python-opster
ttyplay ttyrecord
````

### Remark:
Make sure ````ttyrecord```` is in your present working directory

![alt text](https://github.com/francois-marie/StarExpanders/blob/master/Steiner_tree.png)
![alt text](https://github.com/francois-marie/StarExpanders/blob/master/generalized_entanglement_swapping.png)
