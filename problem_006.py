"""
Problem 6 :

The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
    3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

Solution :
    Sum(n^2) = [n(n+1)(2n+1)]/6
    Sum(n) = [n(n+1)]/2
"""

n = 100

sum_of_squares = (n*(n+1)*(2*n+1))/6
square_of_sums = (n*(n+1)/2)**2

print(int(square_of_sums-sum_of_squares))
