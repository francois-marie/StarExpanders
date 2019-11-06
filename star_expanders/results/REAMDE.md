# Results folder

## What

Contains the ````json```` graph and for each graph a folder with the resulting python & bash scripts

## How

graph_folder created from the id of the network
ex:
````id_network.json````
creates folder
````id````

## Network Structure

````
{
	"Shraddha": {
	    "my_name": "Shraddha",
	    "target": ["Sothy", "FM"],
	    "receivers": 0
	},
	"Sothy": {
	    "my_name": "Sothy",
	    "target": [],
	    "receivers": 2
	},
	"Georg": {
	    "my_name": "Georg",
	    "target": ["Sothy", "FM"],
	    "receivers": 1
	},
	"Fred": {
	    "my_name": "Fred",
	    "target": ["Georg"],
	    "receivers": 0
	},
	"FM": {
	    "my_name": "FM",
	    "target": [],
	    "receivers": 1
	}
}
````