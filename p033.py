"""
https://projecteuler.net/problem=33
"""

import fractions
from fractions import Fraction

def simplify(fraction):    # even easier would be to use fractions library
    numerator = fraction[0]
    denominator = fraction[1]
    
    if denominator == 0:   # invalid fraction
        return None
    if denominator == 1 or numerator == 1:   # already simplified
        return (numerator, denominator)
    
    for n in range(max(numerator, denominator), 0, -1):
        if denominator % n == 0 and numerator % n == 0:
            return (numerator // n, denominator // n)
    
def cancel_digit(numerator, denominator, cancel):
    numerator = str(numerator)
    denominator = str(denominator)
    cancel = str(cancel)

    if cancel in numerator and cancel in denominator:
        num = numerator.replace(cancel, '', 1)  # only replace first instances
        den = denominator.replace(cancel, '', 1)
        return (int(num), int(den))

   
results = Fraction(1, 1)

for d in range(10, 100): # denominators
    for n in range(10, d): # numerators
        for i in str(d): # each index in the denominator
            for j in str(n): # each index in the numerator
                i = int(i)
                j = int(j)
                
                if i == 0 or j == 0 or i != j: # avoid checking zeros in numerator and denominator
                    continue
                
                if simplify((n, d)) == simplify(cancel_digit(n, d, i)):
                    results *= Fraction(n, d)
                    #print(n, d)

print(results.denominator)
