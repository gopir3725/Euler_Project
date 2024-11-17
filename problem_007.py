"""
Problem 7 :

By listing the first six prime numbers: 2, 3, 5, 7, 11 and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""

def get_primes(n):
    n = int(n*np.log(n) + n*np.log(np.log(n)))

    # Assume that all the numbers upto n are prime
    # If they are divisible we will make then non-prime
    prime = [True for i in range(n+1)]

    p = 2
    while (p*p <= n):
        if (prime[p]==True):

            # Update all multiples of p
            for i in range(p*p, n+1, p):
                prime[i] = False

        p+=1

    # Get all prime numbers
    return [p for p in range(2,n+1) if prime[p]]

import numpy as np 
n = 10001
print(get_primes(n)[n-1])
