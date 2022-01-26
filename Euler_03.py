# Solved
from math import *
def isPrime(i):
    for j in range(3,int(sqrt(i))+1,2):
        if(i%j==0):
            return(0)
    return(1)


n=600851475143
h=1
for i in range(3,int(sqrt(n)),2):
    if (n%i==0 and isPrime(i)):
        h=i
print(h)