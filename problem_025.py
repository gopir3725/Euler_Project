"""
Problem 25:

The Fibonacci sequence is defined by the recurrence relation :
    Fn = Fn-1 + Fn+2, where F1 = 1  and F2 = 1

What is the indec of the first term in the series to contain 1000 digits.
"""

# Initializing the terms
a = 1
b = 1

d = 0 # Initializing the no of digits
f = 2 # Initializing the counter

while d<1000:
    # Finding the next term
    c = a + b
    f += 1
    
    # Get digit count
    d = len(str(c))

    # Updating the previous terms
    a = b
    b = c

print(f)
