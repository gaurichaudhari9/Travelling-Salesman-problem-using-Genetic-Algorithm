# -*- coding: utf-8 -*-
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt   
import random
from City import City
class PPath:
   def __init__(self, PathHandler, path=None):
      self.PathHandler = PathHandler
      self.path = []
      self.fitness = 0.0
      self.distance = 0
      if path is not None:
         self.path = path
      else:
         for i in range(0, self.PathHandler.numberOfCities()):
            self.path.append(None)
   
   def __repr__(self):
      geneString = "(City#1=>"
      startCity = self.path[0]
      self.path.append(startCity)
      fig, ax = plt.subplots()
      Path = mpath.Path      
      for i in range(0, self.pathSize()):
         j = i +2
         if i==0 :
            path_data = [
               (Path.MOVETO,(self.getCity(i).getX(),self.getCity(i). getY()))  ]  
         path_data+=[(Path.LINETO, (self.getCity(i).getX(),self.getCity(i). getY()))]
         if i==self.pathSize() :
            path_data+=[(Path.STOP, (self.getCity(i).getX(),self.getCity(i). getY()))]

         geneString += str(self.getCity(i)) + ") ("+"City#"+str(j)+"=>"
      codes, verts = zip(*path_data)
      path = mpath.Path(verts, codes)
      patch = mpatches.PathPatch(path, facecolor='g', alpha=0.1)
      ax.add_patch(patch) 
      #plot control points and connecting lines
      x, y = zip(*path.vertices)
      ine = ax.plot(x, y, 'go-')   
      ax.grid()
      ax.axis('equal')
      plt.show()      
      return geneString
   
    # Creates a random path
   def generateIndividual(self,startCity):
      for cityIndex in range(0, self.PathHandler.numberOfCities()):
         self.setCity(cityIndex, self.PathHandler.getCity(cityIndex))
      random.shuffle(self.path) 
   #force the path to start from given city
      temp = City(self.path[0].getX(),self.path[0].getY())
      for i in range(0,self.pathSize()):
         if startCity.getX() == self.path[i].getX() and  startCity.getY() == self.path[i].getY():
            self.path[i] = temp
            self.path[0] = startCity
            break
   
   #  Gets a city from the path
   def getCity(self, Position):
      return self.path[Position]
   
   # Sets a city in a certain position within a path
   def setCity(self, Position, city):
      self.path[Position] = city
      self.fitness = 0.0
      self.distance = 0
   
   # Gets the tours fitness
   def getFitness(self):
      if self.fitness == 0:
         self.fitness = 1/float(self.getDistance())
      return self.fitness
   
   # Gets the total distance of the path
   def getDistance(self):
      if self.distance == 0:
         pathDistance = 0
         for cityIndex in range(0, self.pathSize()):
            fromCity = self.getCity(cityIndex)
            destinationCity = None
            if cityIndex+1 < self.pathSize():
               destinationCity = self.getCity(cityIndex+1)
            else:
               destinationCity = self.getCity(0)
            pathDistance += fromCity.distanceTo(destinationCity)
         self.distance = pathDistance
      return self.distance
   
   # Get number of cities on our tour
   def pathSize(self):
      return len(self.path)
   
   # Check if the tour contains a city
   def containsCity(self, city):
      return city in self.path

