"""
https://projecteuler.net/problem=63
The 5-digit number, 16807=7**5, is also a fifth power. Similarly, the 9-digit number, 134217728=8**9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

import math

count = 0

for exponent in range(1, 22):
    base = 1

    while(True):
        digits = len(str(base ** exponent))
        if digits == exponent:
            #print(base ** exponent)
            #print(str(base) + " ** " + str(exponent))
            #print("---")
            base += 1
            count += 1
        elif digits > exponent:
            break
        else:
            base += 1
            
print(count)
