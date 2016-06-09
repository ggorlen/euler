"""
https://projecteuler.net/problem=44
"""
import sys
from functools import reduce

"""
from timeit import Timer
    t = Timer("test()", "from __main__ import test")
    print(t.timeit())
"""   

   
def pentagonal(n):
    return int(n * (3 * n - 1) / 2)
    
pentagonals = []
for n in range(1, 1000000):
    pentagonals.append(pentagonal(n))

pentagonals_set = set(pentagonals)

print("Pentagonals set done.")
#print(pentagonals[:300])
# check increment between pentagonals, see what the range for possible addition is and the range for possible subtraction is.

"""
indexes = []
# test area
for j in pentagonals[110000:120000]:   # 110000:120000 was interesting?
    for k in pentagonals[pentagonals.index(j) : pentagonals.index(j) + 10000]:
        if k + j in pentagonals_set:
            indexes.append(pentagonals.index(k) - pentagonals.index(j))
            print("absolute value of k-j: " + str(abs(k - j)))
            print("j: " + str(j) + "   idx:" + str(pentagonals.index(j)))
            print("k: " + str(k) + "   idx:" + str(pentagonals.index(k)))
            print("difference in idx: " + str(pentagonals.index(k) - pentagonals.index(j)))
            print("j + k = " + str(j + k))
            print("j - k idx:" + str(pentagonals.index(k + j)))
            print()
print()            
print(reduce(lambda x, y: x + y, indexes) / len(indexes))
sys.exit()
"""


best = 999999999999
best_j = 0
best_k = 0
index_offset = 0
for k in pentagonals:
    for j in pentagonals[pentagonals.index(k) : pentagonals.index(1): -1]:              # Solution: count backwards in inner loop
        #if k + j in pentagonals_set and pentagonals.index(k) - pentagonals.index(j) < 5:
        #    print("OK" + index_offset)
        #    index_offset += 1
        if k - j in pentagonals_set and j + k in pentagonals_set:
            print(abs(k - j))
            print()
            if abs(k - j) < best:
                best = abs(k - j)
                best_j = j
                best_k = k
                print(best)
                print(best_j)
                print(best_k)
                print()
            
print(best)
print(best_j)
print(best_k)
