"""
Problem 15 :

Starting in the top left corner of a 2 x 2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20 x 20 grid?

Solution :
    In a 2 x 2 grid we will need to take 4 steps to reach the destination.
    Therefore, in a 20 x 20 grid we will have to take 40 steps. The Problem
    amounts to the following : 
    
    "How many different ways can you choose 20 elements out of a set of 40 elements"
    (The elements are: step 1, step 2, etc. and we're choosing, the ones to be incremented)

    Therefore, we can use the following formula :
      
      nCr = n!/(r!(n-r)!)
    40C20 = 40!/(20!(40-20)!)
          = 40!/(20! x 20!)
"""
from math import factorial

grid = 20
no_of_routes = factorial(2*grid)/(factorial(grid)*factorial(20))

print(int(no_of_routes))
