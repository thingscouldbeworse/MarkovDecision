# CS463G Fall 2017 Markov Decision

# Running 

All code is contained in `run.py` and invoked with `python run.py [n|inf]` where `n` is a value to run up until the Vn level. Use `inf` instead if you wish to run the program until it finds an optimal infinite-horizon with the gamma value. Use Ctrl-C to exit early. All code was written and run in Python 3.

# Policy and value functions
`v6.txt` contains the combined policy and value results for running the program to level n=6. `vstar.txt` contains the simmilar results when an infinite-horizon was reached, at level n=436. Below are the results in separate tables.

Note: these tables are formatted in Markdown and look best when viewed in a compatible viewer

|V6 values  |           |           |           |
|-----------|-----------|-----------|---------- |	      	
|95.9344    |138.50774	|207.51444	|284.76245  |
|139.65724  |188.62775  |253.4384	|333.7027   |	       	
|197.88626 	|169.67076	|195.23271	|255.11709  |	       	
|254.82294 	|194.85143 	|155.83594 	|199.76966  |

|V* policies|           |           |           |           |
|-----------|-----------|-----------|-----------|-----------|
|           |   v       |	>       |	>       |   v       |        	
|           |	v       |	>       |	>       |	>       |	
|           |	v       |	<       |	>       |	^       |	
|           |	v       |	<       |	<       |	^       |	

|V* values  |           |           |           |
|-----------|-----------|-----------|---------- |	      	
|869.94267  |921.72497	|991.3845	|1065.83392 |
|913.92062  |968.32066  |1034.06119	|1114.39546 |	       	
|893.50812 	|924.46534 	|973.45701	|1037.95802 |	       	
|933.4205  	|889.78517 	|922.43342 	|986.66824  |	

|V* policies|           |           |           |           |
|-----------|-----------|-----------|-----------|-----------|	
|           |   >       |   >       |   >       |   v       |       	
|           |	>      	|	>  	    |   >      	|	>       | 	
|           |	v      	|	>      	|	>      	|	^       |	
|           |   v      	|	<      	|	>      	|	^       |

# Consultation
I consulted with Grant Sparks on the math approaches to this problem and we compared final value states to ensure we were both on the right track. We identified a flaw in our use of the current value element of the equation, and Grant helped explain the 0.96 gamma value to me. Additionally, the idea for caching individual grids at each n-level so that the recursive function would return if the value was already present (lines 103 and 104 in `run.py` in my final implementation) was given to me by Grant.

# Learned
Having finally taken to heart the meta-lessons of time management and approaches to problem solving mentioned in past assignments, most of my lessons learned here concerned the math itself used to calculate the Markov Decision. The use of a gamma value to bring the value states towards a 'horizon' was a new concept to me, and having seen it in action I feel confident in my ability to use it in another scope/situation. Although it wasn't exactly learned this assignment, the online discussion continued to be very helpful as a large-scale sanity check at multiple stages of the assignment.

# Favorite Thing
I think my favorite thing about this class was the variety of assignment topics and domains covered. In many other CS classes the class ends up in a rut of having one large project due at the end that inevitably feels boring and uninspired by the end of the semester. Each assignment here felt like it was building towards an understanding of the course material, but was complex enough to offer a week of very engaged programming and speculation. 
