"""
https://projecteuler.net/problem=46
"""

import math

def is_prime(n):
    if n == 2 or n ==3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    for i in range(5, int((n ** .5) + 1), 6):
        if n % i == 0:
            return False
        if n % (i + 2) == 0:
            return False
    return True


def is_smallest_odd_composite(n):  # needs optimization
    if not is_prime(n):
        for s in range(1, int(math.sqrt(n))):
            for p in range(n, 1, -2):
                if is_prime(p):
                    #print ("n: " + str(n) + "   p: " + str(p) + "   s: " + str(s))
                    if n == p + 2 * s ** 2:
                        #print("OK")
                        return False
        return True
    return False

    
n = 3
while (True):
    #print(n)
    if is_smallest_odd_composite(n):
        print(n)
        break
    n += 2

