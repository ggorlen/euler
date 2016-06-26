"""
https://projecteuler.net/problem=15
"""

"""
import itertools
#print(len(set(itertools.permutations(['r', 'r', 'd', 'd']))))
p = itertools.permutations(['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd'])

l = []
for permutation in p:
    if permutation not in l:
        l.append(permutation)

print(len(l))


"""
"""
     num paths
0,0  0
0,1  1 <-
0,2  1 <---
1,0  1 <--
1,1  2 <--
1,2  3 <---
2,0  1 <---
2,1  3 <---
2,2  6 <---
"""

import math

side = 20

# combination formula; order doesn't matter
print(math.factorial(side * 2) / (math.factorial(side * 2 - side) * math.factorial(side)))