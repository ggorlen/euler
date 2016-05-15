"""
https://projecteuler.net/problem=32
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

import itertools


products = []

l = [1,2,3,4,5,6,7,8,9]
l = list(itertools.permutations(l))

for n in l:
    if int(str(n[0]) + str(n[1])) * int(str(n[2]) + str(n[3]) + str(n[4])) == int(str(n[5]) + str(n[6]) + str(n[7]) + str(n[8])):
        products.append(int(str(n[5]) + str(n[6]) + str(n[7]) + str(n[8])))

for n in l:
    if int(str(n[0])) * int(str(n[1]) + str(n[2]) + str(n[3]) + str(n[4])) == int(str(n[5]) + str(n[6]) + str(n[7]) + str(n[8])):
        products.append(int(str(n[5]) + str(n[6]) + str(n[7]) + str(n[8])))
            
for n in l:
    if int(str(n[0]) + str(n[1]) + str(n[2])) * int(str(n[3]) + str(n[4]) + str(n[5])) == int(str(n[6]) + str(n[7]) + str(n[8])):
        products.append(int(str(n[6]) + str(n[7]) + str(n[8])))


print(sum(set(products)))