"""
Problem 4 :

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

# Function to chek for palindrome
def is_palindrome(n):
    # Converting the number to string
    n = str(n)

    # Checking if it is a palindrome
    if n == n[::-1]:
        return True
    
    return False

l_palin = 0
for i in range(999,900,-1):
    for j in range(i,900,-1):
        c = int(i*j)
        
        if is_palindrome(c):
            l_palin = c
            break

    if l_palin!=0:
        print(l_palin)
        break
