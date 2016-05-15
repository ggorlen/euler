"""
https://projecteuler.net/problem=43
"""

import itertools


results = []

l = [0,1,2,3,4,5,6,7,8,9]
l = list(itertools.permutations(l))

for n in l:
    if int(str(n[1]) + str(n[2]) + str(n[3])) % 2 == 0 \
    and int(str(n[2]) + str(n[3]) + str(n[4])) % 3 == 0 \
    and int(str(n[3]) + str(n[4]) + str(n[5])) % 5 == 0 \
    and int(str(n[4]) + str(n[5]) + str(n[6])) % 7 == 0 \
    and int(str(n[5]) + str(n[6]) + str(n[7])) % 11 == 0 \
    and int(str(n[6]) + str(n[7]) + str(n[8])) % 13 == 0 \
    and int(str(n[7]) + str(n[8]) + str(n[9])) % 17 == 0:
        results.append(int(str(n[0]) + str(n[1]) + str(n[2]) + str(n[3]) + str(n[4]) + str(n[5]) + str(n[6]) + str(n[7]) + str(n[8]) + str(n[9])))

print(sum(results))