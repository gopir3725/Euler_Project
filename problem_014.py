"""
Problem 14 :

The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n +1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
    13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1 

It can be seen that this sequence (starting at and finishing at ) contains terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def get_chain(n):
    chain = []
    while(n!=1):
        chain.append(n)
        if n%2==0:
            n = n//2

        else:
            n = int(3*n+1)
    
    chain.append(1) 
    return chain

lim = int(1e+6)
max_len = 0
val = 0

for i in range(1,lim,2):
    chain = get_chain(i)
    l = len(chain)

    if l > max_len:
        max_len = l
        val = i

print(val)
