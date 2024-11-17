"""
The sum of the primes below 10 is 
    2 + 3 + 5 + 7 = 17 

Find the sum of all the primes below two million.
"""

# Function to produce prime numbers below n
def get_primes(n):
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

n = int(2E+6)
print(sum(get_primes(n)))


