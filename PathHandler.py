# -*- coding: utf-8 -*-
class PathHandler:
    
   # List that Holds our cities
   destinationCities = []
   
   # Adds a destination city
   def addCity(self, city):
      self.destinationCities.append(city)
   # Get a city
   def getCity(self, index):
      return self.destinationCities[index]
   # Get the number of destination cities
   def numberOfCities(self):
      return len(self.destinationCities)
