"""
Problem 5 :

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Solution :
    1. Find the prime factorization for each number from 1 to 20.
    2. Multiply the greatest power of each prime together.
"""

# Function to get the prime factors and their power
def prime_factors(n,prime):
    power = [0]*len(prime)

    for i,p in enumerate(prime):
        # Finding all the powers of prime factors
        while(n%p==0):
            n = n//p
            power[i]+=1
    
    return power

import numpy as np

# Prime numbers under 20
prime = [2,3,5,7,11,13,17,19]
power = [0]*len(prime)

for i in range(2,20):
    tmp = prime_factors(i,prime)
    
    # Finding the max power of prime factors
    for j in range(len(tmp)):
        if power[j]<tmp[j]:
            power[j]=tmp[j]

# Finding the product of prime factors with their highest power
print(np.prod([i**j for i,j in zip(prime,power)]))
