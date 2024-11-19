"""
Problem 20:

n! means n x (n-1) x ... x 3 x 2 x 1.

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!.
"""

from math import factorial

n = 100
fact = factorial(100)

sum = 0
for d in str(fact):
    sum+=int(d)

print(sum)
