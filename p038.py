"""
https://projecteuler.net/problem=38
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

import itertools


# Readable version of the following list comprehension:
"""
pandigitals = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pandigitals = list(itertools.permutations(pandigitals))              # list() not necessary
pandigitals = [''.join(str(i) for i in x) for x in pandigitals]
pandigitals = [int(i) for i in pandigitals]
"""

pandigitals = [int(i) for i in [''.join(str(i) for i in x) for x in itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9])]]

greatest_pandigitals = []
for n in pandigitals:
    if n // 100000000 == 9:
        greatest_pandigitals.append(n)
    
n = 0
best = 0
test = 0
while test < 999999999:
    test = int(str(n * 1) + str(n * 2))
    if test in greatest_pandigitals:
        print(test)
        print(n)
    if test in greatest_pandigitals and test > best:
        best = test
    n += 1

print("Best: " + str(best))
