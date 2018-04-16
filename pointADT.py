#Kareem Khaled
#khalem1

## @file pointADT.py
#  @title pointADT
#  @author Kareem Khaled
#  @date 2/15/2017

import math

## @brief This class represents a point.
#  @details This class represents a point as an (x,y) coordinate
class PointT:

    ## @brief Constructor for PointT
    #  @details Constructor accepts the two parameters for the x coord and the y coord
    #  @param xc real for the x coordinate
    #  @param yc real for the y coordinate
    def __init__(self, x,y):
        self.xc = x
        self.yc = y

    ## @brief Returns the x coordinate of the point
    #  @return x coordinate of the point
    def xcrd(self):
        return self.xc
        


   ## @brief Returns the y coordinate of the point
   #  @return y coordinate of the point
    def ycrd(self):
        return self.yc



    ## @brief Returns the distance between two points
    #  @details Accepts a point object as input and outputs the distance between the point function is called on
    #  @return real number representing the distance between points is returned
    #  @param p PointT object for any point
    def dist(self, p):
        return math.sqrt( (self.xc - p.xcrd())**2 + (self.yc - p.ycrd())**2 )
    
    ## @brief rotates a PointT point about the origin
    #  @details Accepts real phi as a degree to rotate a point about the origin by.
    #  @param phi real number as a degree to rotate the point by.
    def rot(self,phi):
        self.xc = (math.cos(phi) * self.xc) + (-1*math.sin(phi) * self.yc)
        self.yc = (math.sin(phi) * self.xc) + (math.cos(phi)*self.yc)
