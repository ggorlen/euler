'''
https://projecteuler.net/problem=57
'''

from fractions import Fraction


count = 0
res = 2

for n in range(1000):
    res = 2 + Fraction(1 / res)
    result = Fraction(1 + 1 / res)#.limit_denominator()

    if len(str(result.numerator)) > len(str(result.denominator)):
        count += 1
    
print(count)
