"""
https://projecteuler.net/problem=39
"""

import math

maximum = 0
best = 0
for n in range(0, 1010, 10):
    count = 0
    for x in range(int(math.sqrt(n)), int(n / 2 + 1)):
        for y in range(x, int(n / 2 + 1)):
            for z in range(y, int(n / 2 + 1)):
                if x + y + z == n and x**2 + y**2 == z**2:
                    count += 1
    if count > maximum:
        print(n)
        maximum = count
        best = n
        
print(best)
