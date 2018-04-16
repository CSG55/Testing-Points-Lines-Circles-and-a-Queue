#Kareem Khaled
#khalem1

## @file lineADT.py
#  @title lineADT
#  @author Kareem Khaled
#  @date 2/16/2017

import math
from pointADT import *
## @brief This class represents a line.
#  @details This class represents a line as 2 points
class LineT:



    ## @brief Constructor for lineADT
    #  @details Constructor accepts the two PointT points for the beginning and end points of a line
    #  @param p1 PointT for the beginning point of line
    #  @param p2 PointT for the end point of line
    def __init__(self,p1,p2):
    	self.b = p1
    	self.e = p2


    ## @brief Returns the beginning point of the line
    #  @return beginning point of the line
    def beg(self):
    	return self.b  

    ## @brief Returns the end point of the line
    #  @return end point of the line
    def end(self):
    	return self.e


    ## @brief Returns the length of the line
    #  @details Returns the length of the line as the distance between the start and end points using the dist(p) function of pointADT.py
    #  @return real number coordinate distance between the points 
    def len(self):
    	return self.b.dist(self.e)

    ## @brief Returns the midpoint of the line
    #  @details Returns the averages of the xcords and the ycords added together as a PointT point
    #  @return PointT point as the midpoint of the line

    def mdpt(self):
        newXcord = ((self.b.xcrd()/2.0)+ (self.e.xcrd()/2.0))
        
        newYcord = ((self.b.ycrd()/2.0)+ (self.e.ycrd()/2.0))
        
        newP = PointT(newXcord,newYcord)
        return newP

    ## @brief Rotates line about origin by rotating points 
    #  @details Uses rot(phi) from pointADT.py to rotate the beginning and end points of a LineT line.
    #  @param phi real number to rotate by
    def rot(self,phi):
	    self.b.rot(phi)
	    self.e.rot(phi)

