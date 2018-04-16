#Kareem Khaled
#khalem1

## @file DequeCircleModule.py
#  @title DequeCircleModule
#  @author Kareem Khaled
#  @date 2/19/2017



from circleADT import *


## @brief This class represents a double ended queue of circles
#  @details This class represents a double ended queue of circles with a max size of 20.
class Deq:

    MAX_SIZE = 20
    #q = []


    ## @brief Constructor for Deq
    #  @details Constructor takes no parameters and initializes the queue
    @staticmethod
    def init():
        Deq.q =[]

    ## @brief Adds element to the back of queue
    #  @details Adds element to back of queue if maximum size not exceeded, otherwise FULL exception is raised
    #  @param c for circle to be added to queue
    @staticmethod
    def pushBack(c):
        length = len(Deq.q)
        if length == Deq.MAX_SIZE:
            raise FULL('Queue is at its maximum size of 20')
        Deq.q.append(c)



    ## @brief Adds element to the front of queue
    #  @details Adds element to front of queue if maximum size not exceeded, otherwise FULL exception is raised
    #  @param c for circle to be added to queue
    @staticmethod
    def pushFront(c):
        length = len(Deq.q)
        if length == Deq.MAX_SIZE:
            raise FULL('Queue is at its maximum size of 20')
        Deq.q.insert(0,c)

    ## @brief Removes element from back of queue
    #  @details Removes element from back of queue if queue is not empty, otherwise EMPTY exception is raised
    @staticmethod
    def popBack():
        length = len(Deq.q)
        if length == 0:
            raise EMPTY('Queue is empty, cant pop')
        Deq.q.pop()


    ## @brief Removes element from front of queue
    #  @details Removes element from front of queue if queue is not empty, otherwise EMPTY exception is raised
    @staticmethod
    def popFront():
        length = len(Deq.q)
        if length == 0:
            raise EMPTY('Queue is empty, cant pop')
        Deq.q.pop(0)


    ## @brief Returns element at back of queue
    #  @return element at back of queue
    @staticmethod
    def back():
        length = len(Deq.q)
        if length == 0:
            raise EMPTY('Queue is empty')
        return Deq.q[length-1]


    ## @brief Returns element at front of queue
    #  @return element at front of queue
    @staticmethod
    def front():
        length = len(Deq.q)
        if length == 0:
            raise EMPTY('Queue is empty')
        return Deq.q[0]

    ## @brief Returns number of elements in queue
    #  @details Returns number of circle elements in queue
    #  @return integer number of elements in queue
    @staticmethod
    def size():
        return len(Deq.q)

    ## @brief Returns True if all the circles in the queue are disjoint
    #  @details Returns True if all the circles in the queue are disjoint, or don't intersect
    #  @return boolean for whether or not circles are disjoint
    @staticmethod
    def disjoint():
        length = len(Deq.q)
        cs = Deq.q
        if length == 0:
            raise EMPTY('Queue is empty')

        for c in cs:
            for i in range(length): 
                if c!=cs[i]:
                    return (not c.intersect(cs[i]))


    ## @brief Returns the sum of forces in the x direction
    #  @details Returns the sum of forces in the x direction exerted by all crcles in queue. force(f) is used to calculate this. 
    #  @param f function as gravity function
    #  @return real for sum of forces in x direction
    @staticmethod
    def sumFx(f):
        length = len(Deq.q)
        if length == 0:
            raise EMPTY('Queue is empty')
        def __xcomp(F,ci,cj):
            return F((ci.cen().xcrd()-cj.cen().xcrd())/ci.connection(cj).len())
        #summation variable
        c=0

        #boolean variable to skip first iteration
        c2=0
        for x in range(Deq.size()):
            if c2!=0:
                c+=__xcomp(f,Deq.q[x],Deq.q[0])
            c2+=1
        return c
    







        
        


## @brief This class represents the FULL exception.
#  @details This class represents the FULL exception that is thrown when a circle is added to a queue at its max size.
class FULL(Exception):
    ## @brief Constructor initializes FULL
    #  @param value String representing the error thrown
    def __init__(self, value):
        self.value = value
    ## @brief Returns the String error
    #  @return the string error
    def __str__(self):
        return str(self.value)

## @brief This class represents the EMPTY exception.
#  @details This class represents the EMPTY exception that is thrown when an empty queue is popped.
class EMPTY(Exception):

    ## @brief Constructor initializes EMPTY
    #  @param ivalue String representing the error thrown
    def __init__(self, ivalue):
        self.ivalue = ivalue
        
    ## @brief Returns the String error
    #  @return the string error
    def __str__(self):
        return str(self.ivalue)


