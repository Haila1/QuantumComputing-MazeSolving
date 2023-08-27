# QuantumComputing-MazeSolving
Quantum information scince and quantum computing bootcamp project
Project idea : Solving a maze with quantum simulator
Group members:
Haila Khalaf (leader),
Raghad Alsuhiabni,
Sitah Alotaibi,
Tasneem Alghamdi.

Quantum Algorithm to Solve a Maze : Converting the Maze Problem into a Search Problem

We convert the problem into a Quantum Search Problem (QSP). We encode all possible individual paths from the starting point of the maze into a quantum register. A quantum fitness operator applied on the register encodes each individual with its fitness value. We propose an oracle design which marks all the individuals above a certain fitness value and use the Grover search algorithm to find one of the marked states. Iterating over this method, we approach towards the optimum solution

Individual: One of the members of the population and a candidate for the solution to the Maze problem 
Individual Register: The entire population containing a superposition of all individuals 
Fitness: Measure of how close a particular individual is to the optimal solution. Closer is the individual; higher is its fitness value.

Overview of the used strategy:
1. First step involves the creation of a perfect square maze using the Recursive Backtracker Algorithm
2. Creation of individual register using quantum superposition storing the entire population. 
3. Classifying the individuals based upon their closeness to the optimum solution i.e. defining a fitness register storing the fitness values of individuals. 
4. Defining an Oracle which marks certain individuals having fitness values greater than a threshold fitness value. 
5. Employing Grover’s search algorithm in finding out one of the oracle’s marked states




reference: Quantum Algorithm to Solve a Maze :Converting the Maze Problem into a Search Problem by Debabrata Goswami and Niraj Kumar [https://arxiv.org/pdf/1312.4116.pdf]. 

