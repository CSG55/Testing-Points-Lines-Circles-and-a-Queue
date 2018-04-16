#Kareem Khaled
#khalem1

## @file circleADT.py
#  @title circleADT
#  @author Kareem Khaled
#  @date 2/18/2017

import math
from pointADT import *
from lineADT import *

## @brief This class represents a circle.
#  @details This class represents a line as a center point and a radius.
class CircleT:
    
    ## @brief Constructor for circleADT
    #  @details Constructor accepts a center point PointT and a real number as a radius
    #  @param cin PointT for the center point of the circle
    #  @param rin real for the radius of the circle
    def __init__(self,cin,rin):
    	self.c = cin
    	self.r = rin

    ## @brief Returns the center point of the circle
    #  @return central point of a circle 
    def cen(self):
        return self.c

    ## @brief Returns the radius of the circle 
    #  @return the radius of a circle  
    def rad(self):
        return self.r

    ## @brief Returns the area of a circle
    #  @details Returns the area of a circle using math.pi and the radius squared
    def area(self):
        return math.pi*self.r**2

    ## @brief Returns True only if 2 circles share a point
    #  @param ci CircleT for the second circle that we are comparing to
    #  @return boolean for whether or not 2 circles share a point. 
    def intersect(self,ci):        
            
        p1 = PointT(self.c.xcrd(),self.c.ycrd())
        p2 = PointT(ci.c.xcrd(),ci.c.ycrd())

        
        distance = ((p2.xcrd() - p1.xcrd())**2 + (p2.ycrd() - p1.ycrd())**2)**0.5
        return distance <= self.r + ci.r


            

    ## @brief Returns a LineT line that connects from one circle's center to the input circle's center
    #  @param ci CircleT for the second circle we wish to connect to with a line
    #  @return a LineT line between the circles' centers.
    def connection(self,ci):
        return LineT(self.c, ci.c)



    
    ## @brief Returns a function that ocmputes gravitational force between CircleT and another CircleT
    #  @param f function that takes distance between center of 2 circles
    #  @return lambda function that takes a CircleT circle x as a parameter. 
    def force(self,f):
        return (lambda x: self.area() * x.area()* f(self.connection(x).len()))


    
