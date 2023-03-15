# Travelling-Salesman-problem-using-Genetic-Algorithm


# Genetic Algorithm for TSP

This is an implementation of the Genetic Algorithm for the Traveling Salesman Problem (TSP) in Python. The TSP is a well-known problem in the field of computer science and operations research, where the goal is to find the shortest possible path that visits all cities in a given list exactly once and returns to the starting city.

# Dependencies

Python 3.x
NumPy
Files

City.py - class to represent a city with x and y coordinates
PPath.py - class to represent a path consisting of a sequence of cities
PathHandler.py - class to handle the list of cities and their pairwise distances
Population.py - class to represent a population of paths
GeneticAlgorithm.py - class to handle the genetic algorithm operations
main.py - main file to run the genetic algorithm and display the results
Usage

To run the genetic algorithm with default parameters, simply run the main.py file. You can also modify the parameters in the GeneticAlgorithm constructor in main.py to experiment with different settings. The output will display the best path found by the algorithm, along with its total distance.

# Implementation Details

The genetic algorithm uses a population of paths, where each path represents a possible solution to the TSP. The algorithm evolves the population over a number of generations, selecting the fittest individuals (i.e., those with the shortest distances) to generate offspring through crossover and mutation. The process continues until a termination criterion is met (e.g., a maximum number of generations or a satisfactory fitness level).

In this implementation, the algorithm uses tournament selection to choose parents for crossover, and swap mutation to introduce variation in the population. Elitism is also implemented, where the best individual in the current population is preserved in the next generation. The algorithm starts with a random population of paths and repeats the evolutionary process until convergence.

The algorithm is implemented using object-oriented programming concepts, with separate classes for the city, path, path handler, population, and genetic algorithm. This makes the code modular and easier to maintain and extend.
