from PPath import PPath
#Population  a class that Manages a finite set of candidate paths

class Population:
   
   def __init__(self, PathHandler, populationSize, initialise,startPoint):
      self.paths = []
      self.startPoint = startPoint
      for i in range(0, populationSize):
         self.paths.append(None)
      
      if initialise:
         for i in range(0, populationSize):
            newPath = PPath(PathHandler)
            newPath.generateIndividual(self.startPoint)
            self.savePath(i, newPath)
   
   
   #  Save a Path
   def savePath(self, index, Path):
      self.paths[index] = Path
   
   # Get a Path from population
   def getPath(self, index):
      return self.paths[index]
 
   # Get the best Path in the population
   def getFittest(self):
      fittest = self.paths[0]
      for i in range(0, self.populationSize()):
         if fittest.getFitness() <= self.getPath(i).getFitness():
            fittest = self.getPath(i)
      return fittest
   
   # Get population size
   def populationSize(self):
      return len(self.paths)
