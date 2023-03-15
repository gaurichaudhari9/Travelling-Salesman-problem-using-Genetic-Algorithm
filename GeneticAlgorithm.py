import random
from Population import Population
from PPath import PPath
class GeneticAlgorithm:
   def __init__(self, PathHandler,startPoint):
      self.PathHandler = PathHandler
      self.mutationRate = 0.020
      self.tournamentSize = 5
      self.elitism = True
      self.startPoint = startPoint
   
   # Evolves a population over one generation
   def evolvePopulation(self, pop):
      newPopulation = Population(self.PathHandler, pop.populationSize(), False,self.startPoint)
      # Keep our best individual if elitism is enabled
      elitismOffset = 0
      if self.elitism:
         newPopulation.savePath(0, pop.getFittest())
         elitismOffset = 1
      
      
      for i in range(elitismOffset, newPopulation.populationSize()):
         # Select parents
         parent1 = self.tournamentSelection(pop)
         parent2 = self.tournamentSelection(pop)
         # Crossover parents
         child = self.crossover(parent1, parent2)
         # Add child to new population
         newPopulation.savePath(i, child)
      
      
      for i in range(elitismOffset, newPopulation.populationSize()):
         self.mutate(newPopulation.getPath(i))
            
      return newPopulation
   
  #Applies crossover to a set of parents
   def crossover(self, parent1, parent2):
      #Create new child path
      child = PPath(self.PathHandler)
      child.setCity(0, self.startPoint)
      # Get start and end sub path positions for parent1's path
      startPos = int(random.random() * parent1.pathSize())
      endPos = int(random.random() * parent1.pathSize())
      # Loop and add the sub path from parent1 to our child
      for i in range(0, child.pathSize()):
         # If our start position is less than the end position
         if startPos < endPos and i > startPos and i < endPos and i != 0:
            child.setCity(i, parent1.getCity(i))
         # If our start position is larger
         elif startPos > endPos:
            if i != 0 and  not (i < startPos and i > endPos):
               child.setCity(i, parent1.getCity(i))
      
      # Loop through parent2's city path
      for i in range(0, parent2.pathSize()):
          # If child doesn't have the city add it
         if not child.containsCity(parent2.getCity(i)):
             # Loop to find a spare position in the child's path
            for j in range(0, child.pathSize()):
               # Spare position found, add city
               if child.getCity(j) == None:
                  child.setCity(j, parent2.getCity(i))
                  break
               
      
      return child
   
  # Mutate a path using swap mutation
   def mutate(self, path):
      # Loop through path cities
      for Pos1 in range(1, path.pathSize()):
           # Apply mutation rate
         Pos2 = int(path.pathSize() * random.random())
         if random.random() < self.mutationRate and Pos2 != 0:
            # Get a second random position in the path
            
            
            # Get the cities at target position in path
            city1 = path.getCity(Pos1)
            city2 = path.getCity(Pos2)
            # Swap them around
            path.setCity(Pos2, city1)
            path.setCity(Pos1, city2)
            
   # Selects candidate path for crossover
   def tournamentSelection(self, pop):
      # Create a tournament population
      tournament = Population(self.PathHandler, self.tournamentSize, False,None)
      
      # For each place in the tournament get a random candidate path and add it
      for i in range(0, self.tournamentSize):
         randomId = int(random.random() * pop.populationSize())
         tournament.savePath(i, pop.getPath(randomId))
         
      # Get the fittest path
      fittest = tournament.getFittest()
      return fittest

