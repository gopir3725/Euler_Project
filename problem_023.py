"""
Problem 23:

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

import numpy as np
from math import sqrt
# Function to find the factors of a number
def get_factors(n):
    factors = [1]
    for i in range(2,int(sqrt(n)+1)):
        if n%i==0:
            # Finding the small factors
            factors.append(i)
    
            # Finding the large factors
            if i*i!=n:
                factors.append(n//i)

    return(factors)

lim = 28123

# Finding all the abundant numbers less than or equal to 28123
abundant = []
for i in range(12,lim+1):
    nfact = sum(get_factors(i))

    # Checking if number is abundant
    if nfact>i:
        abundant.append(i)

l = len(abundant)

# Assuming that all numbers are non_abundant_sum
non_abundant_sum = [1]*lim

for i in range(l-1):
    for j in range(i,l):
        
        # Finding the abundant_sum
        val = abundant[i] + abundant[j]
        
        # Stoping criteria if the sum is greater than 28123
        if val >= lim:
            break
        
        # Removing the abundant_sum from non_abundant_sum
        non_abundant_sum[val] = 0

# Finding the sum of non_abundant_sum
s = 0
for i in range(lim):
    if non_abundant_sum[i] == 1:
        s += i

print(s)



