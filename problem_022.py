"""
Problem 22:

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3+15+12+9+14=53, is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
"""

# Scoring function
def get_score(name,idx):
    # Getting the char_value Using the ASCII values
    ch_val = [ord(ch)-64 for ch in name]

    # Finding the score for the name
    score = sum(ch_val)*(idx+1)

    return score


import numpy as np

names = np.loadtxt('data/0022_names.txt',dtype=str,delimiter=',')
names = sorted(names)

total = 0
for idx,name in enumerate(names):
    # Removing the "" in the names
    score = get_score(name[1:-1],idx)
    total += score

print(total)
