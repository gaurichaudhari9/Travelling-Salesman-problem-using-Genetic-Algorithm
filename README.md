# Traveling Salesman Problem with Genetic Algorithm

This code is an implementation of the Traveling Salesman Problem using a genetic algorithm. The goal of the problem is to find the shortest path that visits all cities exactly once and returns to the starting city. The genetic algorithm involves creating a population of paths, selecting the fittest individuals, and creating new generations through crossover and mutation.

# Code structure

- `City.py`: Contains the `City` class which represents a single city with its X and Y coordinates, and methods to calculate the distance to another city and print the city's coordinates.
- `PPath.py`: Contains the `PPath` class which represents a path of cities, and methods to add and get cities, calculate the total distance of the path, and check if a city is already in the path.
- `PathHandler.py`: Contains the `PathHandler` class which handles the cities and paths, and methods to add cities, create a random path, and get the best path.
- `Population.py`: Contains the `Population` class which represents a population of paths, and methods to save and get paths, get the fittest path, and calculate the average fitness of the population.
- `GeneticAlgorithm.py`: Contains the `GeneticAlgorithm` class which implements the genetic algorithm, and methods to evolve a population, select parents through tournament selection, create a child through crossover, and mutate a path.
- `main.py`: Contains the main function to run the genetic algorithm and print the best path.

# Implementation Details

The genetic algorithm uses a population of paths, where each path represents a possible solution to the TSP. The algorithm evolves the population over a number of generations, selecting the fittest individuals (i.e., those with the shortest distances) to generate offspring through crossover and mutation. The process continues until a termination criterion is met (e.g., a maximum number of generations or a satisfactory fitness level).

In this implementation, the algorithm uses tournament selection to choose parents for crossover, and swap mutation to introduce variation in the population. Elitism is also implemented, where the best individual in the current population is preserved in the next generation. The algorithm starts with a random population of paths and repeats the evolutionary process until convergence.


# Usage

1. Clone the repository and navigate to the directory.
2. Run `python main.py` to execute the code.
3. The program will create a `PathHandler` object with six cities and generate a population of paths.
4. The program will then evolve the population over multiple generations using the genetic algorithm.
5. Finally, the program will print the best path found and its distance.


# Dependencies

- Python 3
- math module
- random module

# Contributing

If you find any bugs or have suggestions for improvement, please open an issue or pull request.

# License

This code is released under the MIT License.
