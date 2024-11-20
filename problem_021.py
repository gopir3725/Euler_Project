"""
Problem 21:

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are amicable pair and ech of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1,2,4,5,10,11,20,22,44,55 and 110; therefore d(220) = 284. 
The proper divisors of 284 are 1,2,4,7,71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

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


amicable = set()
for i in range(10000): # 220
    j = sum(get_factors(i)) # 284
    k = sum(get_factors(j)) # 220

    if i==k and i!=j:
        print(i,j)
        amicable.add(i)
        amicable.add(j)

print(sum(amicable))
