# CS463G Fall 2017 Markov Decision

# Running 

All code is contained in `run.py` and invoked with `python run.py [n|inf]` where `n` is a value to run up until the Vn level. Use `inf` instead if you wish to run the program until it finds an optimal infinite-horizon with the gamma value. Use Ctrl-C to exit early. All code was written and run in Python 3.

# Policy and value functions
`v6.txt` contains the combined policy and value results for running the program to level n=6. `vstar.txt` contains the simmilar results when an infinite-horizon was reached, at level n=436. Below| are the results in separate tables

|V* values  |           |           |           |
|-----------|-----------|-----------|---------- |	      	
|869.94267  |921.72497	|991.3845	|1065.83392 |
|913.92062  |968.32066  |1034.06119	|1114.39546 |	       	
|893.50812 	|924.46534 	|973.45701	|1037.95802 |	       	
|933.4205  	|889.78517 	|922.43342 	|986.66824  |	

|V* policies|           |           |           |
|-----------|-----------|-----------|---------- |	
|>          |>          |>          |v          |       	
|	>      	|	>  	    |>       	|	>       | 	
|	v      	|	>      	|	>      	|	^       |	
|v       	|	<      	|	>      	|	^       |