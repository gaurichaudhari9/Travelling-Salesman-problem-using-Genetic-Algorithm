# -*- coding: utf-8 -*-
from City import City
from PathHandler import PathHandler
from Population import Population
from GeneticAlgorithm import GeneticAlgorithm
from PPath import PPath
if __name__ == '__main__':
   
   PathHandler = PathHandler()
   
   # Create and add our cities
   city = City(60, 200)
   PathHandler.addCity(city)
   city2 = City(180, 200)
   PathHandler.addCity(city2)
   city3 = City(80, 180)
   PathHandler.addCity(city3)
   city4 = City(140, 180)
   PathHandler.addCity(city4)
   city5 = City(20, 160)
   PathHandler.addCity(city5)
   city6 = City(100, 160)
   PathHandler.addCity(city6)
   city7 = City(200, 160)
   PathHandler.addCity(city7)
   city8 = City(140, 140)
   PathHandler.addCity(city8)
   city9 = City(40, 120)
   PathHandler.addCity(city9)
   city10 = City(100, 120)
   PathHandler.addCity(city10)
   city11 = City(180, 100)
   PathHandler.addCity(city11)
   city12 = City(60, 80)
   PathHandler.addCity(city12)
   city13 = City(120, 80)
   PathHandler.addCity(city13)
   city14 = City(180, 60)
   PathHandler.addCity(city14)
   city15 = City(20, 40)
   PathHandler.addCity(city15)
   city16 = City(100, 40)
   PathHandler.addCity(city16)
   city17 = City(200, 40)
   PathHandler.addCity(city17)
   city18 = City(20, 20)
   PathHandler.addCity(city18)
   city19 = City(60, 20)
   PathHandler.addCity(city19)
   city20 = City(160, 20)
   PathHandler.addCity(city20)
   city21 = City(30, 40)
   PathHandler.addCity(city21)    
   city22 = City(130, 40)
   PathHandler.addCity(city22)
   city23 = City(110, 40)
   PathHandler.addCity(city23)
   city24 = City(50, 20)
   PathHandler.addCity(city24)
   city25 = City(90, 20)
   PathHandler.addCity(city25)
   city26 = City(170, 20)
   PathHandler.addCity(city26) 
   city27 = City(10, 40)
   PathHandler.addCity(city27)
   city28 = City(135, 40)
   PathHandler.addCity(city28)
   city29 = City(300, 40)
   PathHandler.addCity(city29)
   city30 = City(210, 30)
   PathHandler.addCity(city30)
    
   
   startCity = City(120,80)  #start city 
   
   # Initialize population
   pop = Population(PathHandler, 50, True,startCity);
   #print ("Initial distance: " + str(pop.getFittest().getDistance()))
   
   Algorithm = GeneticAlgorithm(PathHandler,startCity)
   pop = Algorithm.evolvePopulation(pop)
   best_path = PPath(PathHandler)
   best_path = pop.getFittest()
   gen = 0
   for i in range(0, 100):
      pop = Algorithm.evolvePopulation(pop)
      print("Generation#"+str(i)+" =>"+str(pop.getFittest().getDistance()))
      if (best_path.getDistance()>=pop.getFittest().getDistance()):
         best_path = pop.getFittest()
         gen = i
   
   # Print final results
   print ("Final distance: " + str(pop.getFittest().getDistance()))
   print ("Shortest Path for Travelling Sales Person->")
   print (pop.getFittest())
   print("the Optimal Path found in generation: "+str(gen)+" Path Distance : "+str(best_path.getDistance()))
  # print("TSP Path: "+str(best_path))
   
