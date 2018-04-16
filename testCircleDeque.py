#Kareem Khaled
#khalem1

## @file circleADT.py
#  @title circleADT
#  @author Kareem Khaled
#  @date 2/19/2017

import unittest
import math
from circleADT import *
from lineADT import *
from pointADT import *
from deque import *


## @brief This class uses pyunit to test all methods in pointADT
class PointTest(unittest.TestCase):
    ## @brief Conducts tests on every method in pointADT, including edge cases
    def tests(self):
        p1 = PointT(0,2)
        p2 = PointT(0,1)
        
        self.assertTrue(p1.xcrd() == 0)
        self.assertTrue(p1.ycrd() == 2)
        self.assertTrue(p1.dist(p2) == 1)

        
        #Edge cases: rot given a -, +, and 0 radians. Also greater than pi. 
        p1.rot(math.pi/2)
        self.assertTrue(round(p1.ycrd(),1) == -2)
        
        p1.rot(-math.pi/2)
        self.assertTrue(round(p1.ycrd(),1) == 2)

        p1.rot(0)
        self.assertTrue(round(p1.ycrd(),1) == 2)

        p1.rot(2*math.pi)
        self.assertTrue(round(p1.ycrd(),1) == 2)

## @brief This class uses pyunit to test all methods in lineADT
class LineTest(unittest.TestCase):
    ## @brief Conducts tests on every method in lineADT, including edge cases
    def tests(self):
        p1 = PointT(0,2)
        p2 = PointT(0,1)
        p3 = PointT(0,0)
        p4 = PointT(-1,-2)

        l1 = LineT(p1,p2)
        l2 = LineT(p3,p4)

        self.assertTrue(l1.beg()==p1)
        self.assertTrue(l1.end()==p2)
        self.assertTrue(l1.len()==1)
        self.assertTrue(l1.mdpt().xcrd()==0)
        self.assertTrue(l1.mdpt().ycrd()==1.5)
        
        #Edge Case: length of line is 0, find midpoint
        l3 = LineT(p2,p2)
        self.assertTrue(l3.mdpt().xcrd()==0)
        self.assertTrue(l3.mdpt().ycrd()==1)

        
        l1.rot(360)
     
        self.assertTrue(round(l1.beg().xcrd(),2)== round(-1.92,2))
        self.assertTrue(round(l1.end().xcrd(),2)== round(-.96,2))



 

## @brief This class uses pyunit to test all methods in circleADT
class CircleTest(unittest.TestCase):
    ## @brief Conducts tests on every method in circleADT, including edge cases
    def tests(self):
        p1 = PointT(0,2)
        p2 = PointT(0,1)
        p3 = PointT(0,0)
        p4 = PointT(-1,-2)
        
        l1 = LineT(p1,p2)
        l2 = LineT(p3,p4)

        c1 = CircleT(p1,1)
        c2 = CircleT(p2,1)

        self.assertTrue(c1.cen()==p1)
        self.assertTrue(c1.rad()==1)
        self.assertTrue(round(c1.area(),3)==3.142)
        self.assertTrue(c1.intersect(c2)==True)
        self.assertTrue(c1.connection(c2).beg()==LineT(c1.cen(),c2.cen()).beg())
        self.assertTrue(c1.connection(c2).end()==LineT(c1.cen(),c2.cen()).end())

        def __newtheavy(arg):
            return (arg*100)
        
        self.assertTrue(round(c1.force(__newtheavy)(c2),3) == round(986.960440109,3))

## @brief This class uses pyunit to test all methods in deque
class DeqTest(unittest.TestCase):
    ## @brief Conducts tests on every method in deque, including edge cases
    def tests(self):
        p1 = PointT(0,2)
        p2 = PointT(0,1)
        p3 = PointT(0,0)
        p4 = PointT(-1,-2)
        
        l1 = LineT(p1,p2)
        l2 = LineT(p3,p4)

        c1 = CircleT(p1,1)
        c2 = CircleT(p2,1)

        Deq.init()
    
        #Edge case: empty queue, no circles
        with self.assertRaises(EMPTY):
            Deq.popBack()
            
        with self.assertRaises(EMPTY):
            Deq.disjoint()
            

        self.assertTrue(Deq.size()==0)


        Deq.pushFront(c1)
        self.assertFalse(Deq.size()==0)
        Deq.pushBack(c2)
        self.assertTrue(Deq.size()==2)

        Deq.popFront()
        self.assertTrue(Deq.size()==1)
        #Edge case: disjoint with 1 circle
        self.assertFalse(Deq.disjoint()==True)

        
        c4 = CircleT(PointT(999,999),1)
        Deq.pushFront(c4)
        self.assertTrue(Deq.disjoint()==True)
        
        self.assertTrue(Deq.back()==c2)

        #Edge case: full queue, 20 circles already in
        with self.assertRaises(FULL):
            Deq.pushFront(c4)
            Deq.pushFront(c4)
            Deq.pushFront(c4)
            Deq.pushFront(c4)
            Deq.pushFront(c4)
            Deq.pushFront(c4)
            Deq.pushFront(c4)
            Deq.pushFront(c4)
            Deq.pushFront(c4)
            Deq.pushFront(c4)
            Deq.pushFront(c4)
            Deq.pushFront(c4)
            Deq.pushFront(c4)
            Deq.pushFront(c4)
            Deq.pushFront(c4)
            Deq.pushFront(c4)
            Deq.pushFront(c4)
            Deq.pushFront(c4)
            Deq.pushFront(c4)   #21st circle

        self.assertTrue(Deq.front()==c4)

        #sumFx test
        Deq.init()
        Deq.pushFront(c1)
        Deq.pushFront(CircleT(PointT(900,60),900))
        def __newtheavy(arg):
            return (arg*100)
        self.assertTrue(round(Deq.sumFx(__newtheavy),5)==round(-99.7929902533,5))



            
        
if __name__ == '__main__':
    unittest.main()
