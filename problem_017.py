"""
Problem 17:

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 
3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 
115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

def num2words(n):
    ones = {'0': '', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
    special = {'11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'fifteen', '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen'}
    tens = {'0' : '', '1': 'ten', '2': 'twenty', '3': 'thirty', '4': 'fourty', '5': 'fifty', '6': 'sixty', '7': 'seventy', '8': 'eighty', '9': 'ninety'}

    # Converting to string
    s = str(n)
    l = len(s) # number of digits

    word = ''

    if n==1000:
        return 'onethousand'

    # 1's place
    word = ones[s[-1]]

    if l>1:
        # 10's place
        word = tens[s[-2]] + word

        # Handle the special cases
        if s[-2:] in special.keys():
            word = special[s[-2:]]

        if l>2:
            # 100's place
            if word:
                word = ones[s[-3]] + 'hundredand' + word
            else:
                word = ones[s[-3]] + 'hundred'

    return word


    


    # # Only 4-digit number
    # if n==1000:
    #     word = 'onethousand'

    # # 3-digit numbers
    # elif n>=100:
    #     # for i in str(n):
    #         # word += map[i]
    #     word = s[0]+'hundred'

sum = 0
for i in range(1,1001):
    word = num2words(i)
    sum+=len(word)

print(sum)
