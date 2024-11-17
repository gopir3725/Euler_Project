"""
Problem 3 :

The prime factors of 13195 are 5,7,13 and 29.

What is the largest prime factor of the number 600851475143?

Solution :
    If a number N has a prime factor larger than sqrt(N), then it surely has a prime
    factor smaller than sqrt(N). So its sufficient to search for prime factors in the
    range [1,sqrt(N)], and then use them in order to compute the prime factors in the
    range [sqrt(N),N].

    If no prime factors exsists in the range [1,sqrt(N)], then N itself is a prime.
"""

from math import *

# Function to check for prime
def isPrime(i):
    for j in range(3,int(sqrt(i))+1+1,2):
        if(i%j==0):
            return(0)
    return(1)


n=600851475143
lim=int(sqrt(n))+1

p_factors=[]
for i in range(3,lim,2):

    # Checking for prime factor
    if (n%i==0 and isPrime(i)):
        p_factors.append(i)

        # Checking for prime factos above sqrt(n)
        j = i//n
        if j>lim and isPrime(j):
            p_factors.append(j)

print(p_factors)
print(f'Largest prime factor is {max(p_factors)}')
            
        
