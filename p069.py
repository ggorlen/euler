'''
https://projecteuler.net/problem=69
'''

import math


def phi(n):
    count = 0

    for i in range(1, n):
        if math.gcd(i, n) == 1:
            count += 1

    return count
    
    
best_num = 0
best_ratio = 0

for n in range(2310, 1000000, 2310):
    ratio = n / phi(n)

    if ratio > best_ratio:
        best_ratio = ratio
        best_num = n

print(best_num) # TODO 223s
