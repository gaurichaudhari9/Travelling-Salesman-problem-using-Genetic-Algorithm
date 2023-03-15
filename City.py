import math
# City Class to handle only one city(location)
class City:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
      return self.y
  
     # calculate distance from current city to destination city
    def distanceTo(self, city):
      xDistance = abs(self.getX() - city.getX())
      yDistance = abs(self.getY() - city.getY())
      distance = math.sqrt( (xDistance*xDistance) + (yDistance*yDistance) )
      return distance
  
    def __repr__(self):
      return str(self.getX()) + ", " + str(self.getY())